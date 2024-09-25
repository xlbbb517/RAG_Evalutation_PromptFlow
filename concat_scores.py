from promptflow import tool
import json
import re

@tool
def concat_results(similarity_score: str):

    # 解析 JSON 对象
    similarity_json = json.loads(similarity_score)

    load_list = [
        {'name': 'ground_truth', 'score': similarity_json.get("ground_truth", 0)},
        {'name': 'context_question_relevance', 'score': similarity_json.get("context_question_relevance", 0)},
        {'name': 'answer_question_relevance', 'score': similarity_json.get("answer_question_relevance", 0)}
    ]
    score_list = []
    errors = []
    for item in load_list:
        try:
            score = float(item["score"])
        except Exception as e:
            score = None
            errors.append({"name": item["name"], "msg": str(e), "data": item["score"]})
        score_list.append({"name": item["name"], "score": score})

    variant_level_result = {}
    for item in score_list:
        item_name = str(item["name"])
        variant_level_result[item_name] = item["score"]
        # 更新通过门槛值的判断逻辑
        variant_level_result[item_name + '_pass_rate'] = 1 if item["score"] is not None and item["score"] > 0.5 else 0

    return variant_level_result