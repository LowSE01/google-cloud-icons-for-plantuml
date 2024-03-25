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
!include GCPuml/SecretManager.puml

SecretManager(SecretManagerWithDesc, aaa, aaa)
SecretManager(SecretManagerWithoutDesc, aaa)

SecretManagerWithDesc -> SecretManagerWithoutDesc

```

```plantuml

!define GCPuml ../dist
!include GCPuml/GCCommon.puml
!include GCPuml/SecretManager.puml

SecretManagerParticipant(SecretManagerWithDesc, aaa, aaa)
SecretManagerParticipant(SecretManagerWithoutDesc, aaa)

SecretManagerWithDesc -> SecretManagerWithoutDesc

```

```plantuml
!define GCPuml ../dist
!include GCPuml/GCCommon.puml
!include GCPuml/VirtualPrivateCloud.puml
!include GCPuml/Bigquery.puml
!include GCPuml/SecretManager.puml

left to right direction

VirtualPrivateCloudGroup(vpc, Google Cloud) {
    Bigquery(BigQuery, aaa)
    SecretManager(SecretManager, aaa)
    SecretManager --> BigQuery
}
```