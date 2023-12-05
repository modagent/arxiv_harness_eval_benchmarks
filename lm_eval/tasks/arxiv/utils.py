import datasets

def process_docs(dataset: datasets.Dataset):
    def _helper(doc):
      # modifies the contents of a single
      # document in our dataset.
      doc["gold"] = doc["ideal"].lower()
      return doc

    return dataset.map(_helper) # returns back a datasets.Dataset object