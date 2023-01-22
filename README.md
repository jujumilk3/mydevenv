# mydevenv

## default `.env`
```dotenv
ENV=dev
JWT_SECRET_KEY=mydevenv
```

## dispose Tool and ToolTag Relation
```mermaid
graph TD

    A[Tool] --> B[ToolTag]
    B --> C[Tag]
```
