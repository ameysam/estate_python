class Manager:
    def __init__(self, _class=None):
        self._class = _class

    def __str__(self):
        return f"Class {self._class}"

    def search(self, **kwargs):
        results = list()

        for obj in self._class.object_list:
            comparation_results = list()
            for key, value in kwargs.items():
                if key.endswith('__min'):
                    key = key[:-5]
                    compare_key = 'min'
                elif key.endswith('__max'):
                    key = key[:-5]
                    compare_key = 'max'
                else:
                    compare_key = 'equal'

                if hasattr(obj, key):
                    if compare_key == 'min':
                        # add the comparation result to comparation_results list
                        comparation_results.append(getattr(obj, key) >= value)
                    elif compare_key == 'max':
                        # add the comparation result to comparation_results list
                        comparation_results.append(getattr(obj, key) <= value)
                    else:
                        # add the comparation result to comparation_results list
                        comparation_results.append(getattr(obj, key) == value)

            # If comparation_results True items count equal with len of search args,
            # then search add found item to main search results
            if sum(comparation_results) == len(kwargs):
                results.append(obj)


        return results
