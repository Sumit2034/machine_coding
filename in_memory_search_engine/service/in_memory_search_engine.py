class InMemorySearchEngine:
    def __init__(self, namespace):
        # to track namespace and its documents
        self.namespace = namespace

    # add documents to the namespace
    def add_documents(self, namespace, *documents):
        if namespace not in self.namespace:
            # if the namespace does not exist, create one and add the documents
            self.namespace[namespace] = list(documents)
        else:
            # else add and merge the documents
            self.namespace[namespace].extend(documents)

    # search the documents of the given namespace
    def search(self, namespace, filter_fn, order_by_fn=None):
        # get the namespace
        docs = self.namespace.get(namespace, [])

        # get it filtered
        filtered = list(filter(filter_fn, docs))

        # if order_by is requested
        if order_by_fn:
            key, asc = order_by_fn

            # order by the searched result
            # based on the key and order requested
            filtered.sort(key=lambda x: x[key], reverse=not asc)

        return filtered

    def search_key_in_doc(self, namespace, key):
        # get the namespace
        docs = self.namespace.get(namespace, [])
        res = []
        # get it filtered
        for doc in docs:
            for value in doc.values():
                if key in value:
                    res.append(doc)
        
        return res

    def search_order_by(self, namespace, key):
        # get the namespace
        docs = self.namespace.get(namespace, [])
        res = []
        # get it filtered
        for doc in docs:
            for value in doc.values():
                if key in value:
                    res.append(doc)
        
        return res
