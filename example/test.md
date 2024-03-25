# AWS Icons for Plantuml

```plantuml
!define AWSPuml https://raw.githubusercontent.com/awslabs/aws-icons-for-plantuml/v18.0/dist
!include AWSPuml/AWSCommon.puml
!include AWSPuml/Groups/AWSCloud.puml
!include AWSPuml/Analytics/Redshift.puml

left to right direction
AWSCloudGroup(cloud) {
    Redshift(Redshift, aaa,  aaa , aaa)
    aa --> Redshift
}

```


# Google Cloud Icons for Plantuml

```plantuml
!define GCPuml ../dist
!include GCPuml/GCCommon.puml
!include GCPuml/VirtualPrivateCloud.puml
!include GCPuml/Bigquery.puml
!include GCPuml/SecretManager.puml

left to right direction

VirtualPrivateCloudGroup(vpc, aaaaa) {
    Bigquery(BigQuery, aaa, aaa, aaa)
    SecretManager(SecretManager, aaa, aaa, aaa)
    SecretManager --> BigQuery
}
```