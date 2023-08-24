from collections import namedtuple

DataIngestionConfig = namedtuple("DatasetConfig",['dataset_download_url',
                                                  'raw_data_Dir',
                                                  'ingestioned_dir'])