from jina import Flow
from docarray import DocumentArray

f = (Flow()
     .add(uses='single_file_executor/config.yml')
     .add(uses='multi_files_executor/config.yml'))

with f:
    f.post(on='/foo', inputs=DocumentArray.empty())