# Google Cloud Icons for Plantuml

## Component Diagram

```plantuml

!define GCPuml ../dist

!include GCPuml/GCCommon.puml

!include GCPuml/Bigquery.puml
!include GCPuml/CloudRun.puml
!include GCPuml/CloudStorage.puml
!include GCPuml/SecretManager.puml

Bigquery(BigQuery, bq)
CloudRun(CloudRun, job)
CloudStorage(CloudStorage, gcs)
SecretManager(SecretManager, secrets)

CloudRun .d.> BigQuery
CloudRun .d.> CloudStorage
CloudRun .r.> SecretManager
CloudStorage -r-> BigQuery

```

## Sequence Diagram

```plantuml

!define GCPuml ../dist
!include GCPuml/GCCommon.puml

!include GCPuml/Bigquery.puml
!include GCPuml/CloudRun.puml
!include GCPuml/CloudStorage.puml
!include GCPuml/SecretManager.puml

CloudRunParticipant(CloudRun, job)
SecretManagerParticipant(SecretManager, secrets)
CloudStorageParticipant(CloudStorage, gcs)
BigqueryParticipant(BigQuery, bq)

CloudRun -> SecretManager: get
Activate CloudRun
CloudRun <-- SecretManager

CloudRun -> CloudStorage: read
CloudRun <-- CloudStorage

CloudRun -> BigQuery: write
Activate BigQuery
CloudRun <-- BigQuery
Deactivate BigQuery

Deactivate CloudRun

```
