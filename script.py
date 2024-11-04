from datafog import DataFog
from datafog.config import OperationType
from datafog.models.spacy_nlp import SpacyAnnotator
from datafog.models.anonymizer import Anonymizer, AnonymizerType

client = DataFog(operations=[OperationType.SCAN, OperationType.REDACT])

text = "Tim Cook is the CEO of Apple and is based out of Cupertino, California"

# README Implementation
redacted_text = client.run_text_pipeline_sync([text])[0]
print(redacted_text)

# Correct Implementation
# annotator = SpacyAnnotator()
# anonymizer = Anonymizer(anonymizer_type=AnonymizerType.REDACT)
# annotations = annotator.annotate_text(text)
# result = anonymizer.anonymize(text, annotations)
# print(result.anonymized_text)