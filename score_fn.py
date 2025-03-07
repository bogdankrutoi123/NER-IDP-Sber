def score_fn(gold: str, pred: str) -> float:
    """
    Преобразует данные с выделенными сущностями и считает F1-score для предсказаний модели.

    :param gold: идеальные предсказания
    :param pred: предсказания модели
    :return: F1-score
    """

    gold = set(tuple(s.split('\t')) for s in gold.split('\n'))
    pred = set(tuple(s.split('\t')) for s in pred.split('\n'))

    tp = len(gold & pred)
    fp = len(pred - gold)
    fn = len(gold - pred)

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    return f1

def score_fn_for_category(gold: str, pred: str, cat: str) -> float:
    """
    Преобразует данные с сущностями, отбирает конкретные упоминания по типу сущности cat
     и считает F1-score для предсказаний модели.

    :param gold: идеальные предсказания
    :param pred: предсказания модели
    :param cat: категория сущности
    :return: F1-score
    """

    gold = set(tuple(s.split('\t')) for s in gold.split('\n') if s.endswith(cat))
    pred = set(tuple(s.split('\t')) for s in pred.split('\n') if s.endswith(cat))

    if len(gold) == 0 and len(pred) == 0:
        return 1.0

    tp = len(gold & pred)
    fp = len(pred - gold)
    fn = len(gold - pred)

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    return f1
