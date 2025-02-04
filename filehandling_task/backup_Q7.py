"""
q7 If you were developing a backup system, how would you handle file read/write operations 
to ensure data integrity and avoid corruption?

1. Atomic operations -ensure that file changes are either fully completed or not done at all, preventing partial backups by using temporary files and renaming them.

2. File locking- prevents multiple processes from accessing the same file simultaneously, avoiding corruption from concurrent operations.

3. Checksum validation- verifies the integrity of both the original and backup files by generating and comparing checksums, ensuring no corruption occurs.

4. Breaking large files into smaller chunks- makes it easier to handle failures, as each chunk can be verified and retried without affecting the entire file.

5. Error handling and retry mechanisms- ensure temporary issues (e.g., network failures or disk space problems) don’t lead to corrupted backups by retrying operations.

6. Transactional backups-, where changes are logged and can be rolled back if a failure occurs, maintain consistency and prevent incomplete backups.

7. Versioning and incremental backups- allow for maintaining multiple backup versions, minimizing the risk of corruption and enabling restoration of earlier, uncorrupted versions.

8. Monitoring and logging- track all backup operations to detect issues early, while **regular integrity checks** ensure backups remain intact and can be restored when needed.
"""