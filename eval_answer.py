def _cos_sim(a, b):
    from numpy import dot
    from numpy.linalg import norm
    divider = norm(a) * norm(b)
    if abs(divider) < 1e-6:
        return 0
    return dot(a, b) / divider


def anser_sim(a, b, text2vec_model):
    if len(a) == 0 and len(b) == 0:
        return -1
    if len(a) == 0 or len(b) == 0:
        return -1

    embeddings = text2vec_model.encode([a, b])
    cos_sim = _cos_sim(embeddings[0], embeddings[1])
    return cos_sim