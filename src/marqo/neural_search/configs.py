from marqo.neural_search import enums as ns_enums
from marqo.neural_search.enums import NeuralSettingsField as NsFields
import marqo.enums as mq_enums
from torch import multiprocessing as mp

def get_default_neural_index_settings():
    # if new fields are added, also update index.py to take in the new params
    return {
        NsFields.index_defaults: {
            NsFields.treat_urls_and_pointers_as_images: False, # only used for models that have text and vision encoders
            NsFields.model: ns_enums.MlModel.bert,
            NsFields.normalize_embeddings: True,
            NsFields.text_preprocessing: {
                NsFields.split_length: 2,
                NsFields.split_overlap: 0,
                NsFields.split_method: ns_enums.SplitMethod.sentence
            },
            # TODO move these into a processing dict with sub-dicts
            NsFields.image_preprocessing:{
                NsFields.patch_method: None #
                    }
        }
    }

def get_max_processes():
    return {'max_processes_cpu' :6, 'max_processes_gpu': 2}

def get_threads_per_process():
    total_cpu = max(1, mp.cpu_count() - 2)
    return max(1, total_cpu//get_max_processes()['max_processes_cpu'])
