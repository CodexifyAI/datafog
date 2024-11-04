from datafog import DataFog
from datafog.config import OperationType
from datafog.models.anonymizer import Anonymizer, AnonymizerType
from datafog.models.spacy_nlp import SpacyAnnotator

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


# Sample redaction using DataFog main.py implementation
sample_texts = [
    "John Smith lives at 123 Main St in New York",
    "Contact Sarah Jones at sarah.jones@email.com or (555) 123-4567",
    "SSN: 123-45-6789 belongs to Michael Wilson",
]

# Initialize DataFog with SCAN and REDACT operations
datafog_client = DataFog(operations=[OperationType.SCAN, OperationType.REDACT])

# Process multiple texts synchronously
redacted_results = datafog_client.run_text_pipeline_sync(sample_texts)

print("Original vs Redacted texts:")
for original, redacted in zip(sample_texts, redacted_results):
    print("\nOriginal:", original)
    print("Redacted:", redacted)
