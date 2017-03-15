---
Description: The Base schema defines elements that are used to describe basic data types used throughout the Mobile Broadband schema. It defines only simple and complex types.
MS-HAID: Base.Schema\_Root
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: Base schema
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c
author: mcleblanc
ms.author: markl
keywords: windows 10
---

# Base schema


The Base schema defines elements that are used to describe basic data types used throughout the Mobile Broadband schema. It defines only simple and complex types. All of the types within the Base schema are documented as elements within the other Mobile Broadband schema.

The full Base schema is below:

``` syntax
<?xml version="1.0" encoding="utf-8"?>  
<xs:schema targetNamespace="http://www.microsoft.com/networking/CarrierControl/Base/v1"  
    elementFormDefault="qualified"  
    xmlns="http://www.microsoft.com/networking/CarrierControl/Base/v1"  
    xmlns:xs="http://www.w3.org/2001/XMLSchema">  
 
  <xs:simpleType name="NameType">  
    <xs:restriction base="xs:normalizedString">  
      <xs:minLength value="1"/>  
      <xs:maxLength value="255"/>  
      <xs:whiteSpace value="collapse"/>  
    </xs:restriction>  
  </xs:simpleType>  
  
  <xs:simpleType name="Priority">  
    <xs:restriction base="xs:nonNegativeInteger">  
      <xs:maxExclusive value="10"/>  
    </xs:restriction>  
  </xs:simpleType>  
  
  <xs:simpleType name="GUID">  
    <xs:annotation>  
      <xs:documentation xml:lang="en">  
        The representation of a GUID, generally the id of an element.  
      </xs:documentation>  
    </xs:annotation>  
    <xs:restriction base="xs:token">  
      <xs:pattern value="\{[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\}"/>  
    </xs:restriction>  
  </xs:simpleType>  
  
  <xs:simpleType name="SubscriberType">  
    <xs:restriction base="xs:token">  
      <xs:maxLength value="20"/>  
      <xs:pattern value="\w+"/>  
    </xs:restriction>  
  </xs:simpleType>  
  
  <xs:complexType name="CertificateDetails">  
    <xs:annotation>  
      <xs:documentation>  
        Used to identify a certificate or set of certificates.  SubjectName is compared against  
        the DN provided as the certificate's Subject field, or against any Name provided in the  
        SubjectAlternativeName extentions of type DirectoryName.  IssuerName is compared against  
        the DN provided as the certificate's Issuer field, or against any Name provided in the  
        IssuerAlternativeName extentions of type DirectoryName.  
      </xs:documentation>  
    </xs:annotation>  
    <xs:sequence>  
      <xs:element type="xs:string" name="SubjectName"/>  
      <xs:element type="xs:string" name="IssuerName"/>  
    </xs:sequence>  
  </xs:complexType>  

  <xs:simpleType name="ProviderNameType">  
    <xs:restriction base="xs:normalizedString">  
      <xs:minLength value="1"/>  
      <xs:maxLength value="20"/>  
      <xs:whiteSpace value="collapse"/>  
    </xs:restriction>  
  </xs:simpleType>  
  
  <xs:simpleType name="ProviderIdType">  
    <xs:restriction base="xs:token">  
      <xs:pattern value="\d{1,6}"/>  
    </xs:restriction>  
  </xs:simpleType>  
  
  <xs:complexType name="ProviderType">  
    <xs:sequence>  
      <xs:element name="ProviderID" type="ProviderIdType"/>  
      <xs:element name="ProviderName" type="ProviderNameType"/>  
    </xs:sequence>  
  </xs:complexType>  
</xs:schema>
```

 

 



