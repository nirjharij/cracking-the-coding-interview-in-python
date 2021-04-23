from collections import defaultdict, Counter

word_map = defaultdict(list)


def sparse_sim(data):
    for i, v in data.items():
        for word in v:
            word_map[word].append(i)

    output = {}
    for i, v in data.items():
        docs_list = []
        for word in v:
            docs_list.extend(word_map[word])

        doc_counts = Counter(docs_list)

        for doc, val in doc_counts.items():
            similarity = val / (len(v) + len(data[doc]))
            if similarity > 0:
                if i == doc:
                    continue
                elif (i, doc) in output or (doc, i) in output:
                    continue
                output[(i, doc)] = similarity

    print(output)


sparse_sim({13: [14, 15, 100, 9, 3], 16: [32, 1, 9, 3, 5], 19: [15, 29, 2, 6, 8, 7], 24: [7, 10]})
