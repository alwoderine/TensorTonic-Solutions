def deduplicate(records, key_columns, strategy):
    """
    Deduplicate records by key columns using the given strategy.
    """
    def keep_first(records, key_columns):
        seen = set()
        res = []
        for rec in records:
            id = tuple(rec[col] for col in key_columns)
            if id in seen:
                continue
            res.append(rec)
            seen.add(id)
        print(seen)
        return res

    def keep_last(records, key_columns):
        seen = {} # {(id, name) : idx of insertion in res}
        res = []
        for rec in records:
            id = tuple(rec[col] for col in key_columns)
            if id in seen:
                # replace existing with new one
                idx = seen[id]
                res[idx] = rec
            else:
                seen[id] = len(res)
                res.append(rec)
        return res


    def keep_most_complete(records, key_columns):
        seen = {}
        res = []
        for rec in records:
            id = tuple(rec[col] for col in key_columns)
            if id in seen:
                idx = seen[id][0]
                n_none = seen[id][1]

                curr_none = len([val for val in rec.values() if val == None])

                if n_none > curr_none:
                    res[idx] = rec
                    seen[id][1] = curr_none
            else:
                curr_none = len([val for val in rec.values() if val == None])
                idx = len(res)
                seen[id] = [idx, curr_none]
                res.append(rec)
        return res

    callables = {
        "first": keep_first,
        "last": keep_last,
        "most_complete": keep_most_complete
    }

    return callables[strategy](records, key_columns)

        

            