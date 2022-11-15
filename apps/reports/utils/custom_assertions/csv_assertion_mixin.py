from csv import DictReader

class CsvAssertionMixin():
        
    def assertHeadersExist(self, csv: DictReader, *headers_to_assert: list):
        csv_headers = list(csv).pop(0)
        
        for idx, header in enumerate(headers_to_assert):
            if not csv_headers[idx] == header:
                raise AssertionError(f'Header {header} does not exist')