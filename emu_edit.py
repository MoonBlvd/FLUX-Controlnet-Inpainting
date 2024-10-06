from datasets import load_dataset

ds = load_dataset("facebook/emu_edit_test_set")
import ipdb; ipdb.set_trace()
ds["test"].__getitem__(0)