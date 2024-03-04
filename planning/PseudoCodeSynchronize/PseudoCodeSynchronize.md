

1. Generate checkSums Object.
2. Recursively iterate all files in **replica**
    1. For every file get its **MD5**
    2. Save first file path in origin.
    3. Save path in replica SET.
3. Recursively iterate all files in **source**
    1. For every file get its **MD5**
    2. Save first file path in origin.
    3. Save path in source SET.

The object will look something like:

```objectcode
{'md5key1': 
    {origin: 'pathFirstFile',
    replicas: Set of replicas Path,
    source: Set of source Path,
    },
'md5key2': {...},
'md5key3': {...},
...
}
```

If there are same files in both folders, the one from replica will be used to copy.

4. For each MD5 key in the object
    1. Remove duplicates from both sets
    2. For each file in source SET
        1. Check if there is a file with same name and rename it to a temp name
        2. Copy file from origin
    3. For each file in replica SET remove it

(Check point 4 images)

5. Recursively generate empty folders