# ADR-002: Data Storage Strategy

## Status
Accepted

## Context
The pytorch-workflow project requires a data storage strategy to efficiently manage and retrieve large amounts of data, including model weights, training metadata, and user input. The chosen strategy must integrate with the existing tech stack, including Python, FastAPI, PostgreSQL, Redis, and Docker.

## Decision
We decided to use a hybrid approach, leveraging PostgreSQL for structured data and Redis for caching and transient data, while utilizing Docker for containerization and ensuring consistency across environments.

## Alternatives Considered
* **Relational Database Only**: Using only PostgreSQL for all data storage needs, which would lead to increased complexity and reduced performance for non-structured data.
* **NoSQL Database**: Utilizing a NoSQL database, such as MongoDB, for all data storage needs, which would require significant changes to the existing tech stack and might not provide the necessary structure for certain data types.
* **Cloud-based Object Storage**: Using cloud-based object storage, such as AWS S3, for storing model weights and other large files, which would introduce additional dependencies and require additional configuration.

## Consequences
The hybrid approach provides a balance between structure and flexibility, allowing for efficient data retrieval and storage. However, it also introduces additional complexity in terms of data consistency and synchronization between PostgreSQL and Redis. The use of Docker ensures consistency across environments, but may require additional resources for container management. Overall, the chosen strategy should provide a good tradeoff between performance, scalability, and maintainability.