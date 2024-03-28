# Google Cloud Icons for Plantuml

## Component Diagram

```plantuml

skinparam linetype ortho

' !define AWSPuml https://raw.githubusercontent.com/awslabs/aws-icons-for-plantuml/main/dist

' !include AWSPuml/AWSCommon.puml
' !include AWSPuml/Groups/AWSCloud.puml
' !include AWSPuml/Analytics/Redshift.puml

' AWSCloudGroup(AWSCloud) {
'     Redshift(Redshift, "Redshift",)
' }

!define GCPuml ../dist
!include GCPuml/GCCommon.puml

!include GCPuml/Bigquery.puml
!include GCPuml/CloudRun.puml
!include GCPuml/CloudStorage.puml
!include GCPuml/MyCloud.puml
!include GCPuml/Looker.puml
!include GCPuml/SecretManager.puml


MyCloudGroup(GoogleCloud, "Google Cloud") {
    Bigquery(BigQuery, bq)
    CloudRun(CloudRun, job)
    CloudStorage(CloudStorage, gcs)
    SecretManager(SecretManager, secrets)
    Looker(Looker, visualize)
}

CloudRun .d.> BigQuery
CloudRun .d.> CloudStorage
CloudRun .r.> SecretManager
CloudStorage -r-> BigQuery
Looker .l.> BigQuery

```

## Sequence Diagram

```plantuml

' !define AWSPuml https://raw.githubusercontent.com/awslabs/aws-icons-for-plantuml/main/dist

' !include AWSPuml/AWSCommon.puml
' !include AWSPuml/Analytics/Redshift.puml

' RedshiftParticipant(Redshift, db,)

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
