Title: DynamoDB with Automatic Blob Fields in S3
Date: 2025-08-16 09:45
Category: Blog
Tags: Claude Code, DynamoDB, AWS, python, largelanguagemodels

A pattern I like to use for data storage is to keep the metadata in DynamoDB and the larger content in S3, with links in
the DB item pointing to the corresponding S3 keys. This approach can give DynamoDB queries a huge boost in speed and
cost savings, since you can process a lot more records at a time when you just need metadata and not the full content.

The challenge, of course, is that it can be a bit of a hassle to set up, and until recently I hadn’t really worked out a
clean pattern I felt great about. What I’ve always wanted was to fully automate this—so that I could simply flag a field
on my resource class definition as a “blob,” and it would automatically be saved in S3 instead of in the DynamoDB item.

Here’s what that looks like now:

```python
class DemoVersionedResourceWithBlobs(DynamoDbVersionedResource):
    """Test versioned resource with a "blob" field."""

    title: str
    metadata: dict
    document_content: Optional[str] = None  # Blob field

    resource_config: ClassVar[ResourceConfig] = ResourceConfig(
        compress_data=False,
        max_versions=5,
        blob_fields={
            "document_content": BlobFieldConfig(
                compress=True,
                content_type="text/plain"
            )
        }
    )
```

With this setup I can query items without loading document_content, and then only fetch it on demand for specific items.

## Building with AI

I’ve been working with Claude Code to add several features to my
personal [DynamoDB library](https://github.com/msull/simplesingletable), and yesterday I tackled this “blob fields”
feature. It’s just as awesome as I had always imagined it would be.

I’ll start integrating it into my production code base next week and really put it through its paces, but early testing
and benchmarking look great. For my most frequent use cases, I think it’s going to be very effective-- particularly for
some of the daily compliance reporting data we pull, where we only care about a handful of fields most of the time but
still need to retain a big data dump per individual.

One of the biggest benefits of working with Claude is that it’s helping me finally clear out a backlog of long-standing
feature requests in my library, things I never felt I had to time to work on. Now I just focus on design, testing, and
implications, while the AI handles most of the coding, and it has been a great accelerator.

## Benchmark Results (2500 items)

* [Benchmark Script](https://github.com/msull/simplesingletable/blob/main/tests/test_blob_storage_performance.py)

| Metric                   | 1KB   | 4KB   | 16KB   | 32KB   |
|---------------------------|-------|-------|--------|--------|
| Create Time w/o Blob (ms) | 9227  | 8330  | 8170   | 8578   |
| Create Time w/ Blob (ms)  | 14403 | 14393 | 14448  | 15110  |
| Create Overhead           | 56.1% | 72.8% | 76.8%  | 76.1%  |
| Query Time w/o Blob (ms)  | 184   | 280   | 1527   | 4100   |
| Query Time w/ Blob (ms)   | 150   | 124   | 140    | 139    |
| Query Time Savings        | 18.5% | 55.8% | 90.8%  | 96.6%  |
| RCUs w/o Blob             | 416   | 1356  | 5119   | 10118  |
| RCUs w/ Blob              | 103   | 103   | 103    | 103    |
| RCU Savings               | 75.2% | 92.4% | 98.0%  | 99.0%  |
| API Calls w/o Blob        | 4     | 11    | 40     | 79     |
| API Calls w/ Blob         | 1     | 1     | 1      | 1      |
