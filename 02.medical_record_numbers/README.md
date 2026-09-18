# Medical Record Numbers (MRN)

An exercise on deduplication, based on a true story.

The file `mrn.txt` contains several lines, each with a variable number of mrn numbers. All the numbers in a line correspond to the same patient. But a number can appear in different lines, so that all numbers in them point to the same patient.

- How many unique patients are there?
- Assign a random ID number to every unique patient and write it alongside every number associated to them (in `mrn_unique.txt`).

```Bash
python deduplicate.txt

Out of 1000 lines, there are just 123 unique patients
```

