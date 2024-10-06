from model.name_space import NameSpace
from service.in_memory_search_engine import InMemorySearchEngine


def main():
    namespace = NameSpace()
    # Register namespaces
    ns = namespace.register_namespace('employees')
    search_engine = InMemorySearchEngine(namespace=ns)

    # Add documents to the namespace
    search_engine.add_documents('employees',
        {'name': 'Mario', 'age': 27, 'salary': 5000000},
        {'name': 'Lisa', 'age': 30, 'salary': 15000000},
        {'name': 'Soham', 'age': 54, 'salary': 25000000},
        {'name': 'Shyam', 'age': 52, 'salary': 35000000}
    )

    # Search with a filter function
    results = search_engine.search('employees', lambda x: x['age'] > 30)

    print("Filtered results:", results)

    # Search with filter and order by function
    results = search_engine.search('employees', lambda x: x['age'] > 30, ('salary', True))

    print("Filtered and ordered results:", results)

    # Register namespaces
    ns = namespace.register_namespace('documents')
    search_engine = InMemorySearchEngine(namespace=ns)
    
    # Add documents to the namespace
    search_engine.add_documents('documents',
        {'DOC1': "eat apple daily" },
        {'DOC2': "eat banana daily" },
        {'DOC3': "one apple daily" },
        {'DOC4': "eat orange daily" }
    )

    # Search with a filter function
    results = search_engine.search_key_in_doc('documents', 'apple')

    print("Filtered results:", results)


if __name__ =='__main__':
    main()