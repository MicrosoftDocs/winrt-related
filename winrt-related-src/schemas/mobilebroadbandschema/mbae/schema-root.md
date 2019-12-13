---
Description: The Mobile Broadband Account Experience (MBAE) schema defines elements that are used by mobile network operators and retail partners to deliver valued added services to customers.
Search.Product: eADQiWindows 10XVcnh
title: MBAE schema
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# MBAE schema


The Mobile Broadband Account Experience (MBAE) schema defines elements that are used by mobile network operators and retail partners to deliver valued added services to customers. All of the elements are in the namespace http://schemas.microsoft.com/windows/2010/12/DeviceMetadata/MobileBroadbandInfo. Not all elements are in every profile, as some elements are optional.

The following table lists all of the elements in this schema, sorted alphabetically by name.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="element-internet.md">Internet</a> </td>
<td><div class="alert">
<strong>Note</strong>  The <strong>Internet</strong> element is deprecated. Starting with Windows 8 and Windows Server 2012, the mobile operator should use Access Point Name (APN) Database to provide Internet APN information.
</div>
<div>
 
</div>
<p>Defines the mobile broadband Internet profile to be used for the mobile network.</p></td>
</tr>
<tr class="even">
<td><a href="element-issuername.md">IssuerName</a> </td>
<td><p>Defines the issuer name of the trusted certificate.</p></td>
</tr>
<tr class="odd">
<td><a href="element-mobilebroadbandinfo.md">MobileBroadbandInfo</a> </td>
<td><p>Defines mobile broadband information required for provisioning on the mobile network.</p></td>
</tr>
<tr class="even">
<td><a href="element-mobilebroadbandprofiles.md">MobileBroadbandProfiles</a> </td>
<td><div class="alert">
<strong>Note</strong>  The <strong>MobileBroadbandProfiles</strong> element is deprecated. Starting with Windows 8 and Windows Server 2012, the mobile operator should use Access Point Name (APN) Database to provide Internet and Purchase APN information.
</div>
<div>
 
</div>
<p>Defines the mobile broadband Purchase and Internet profiles to be used for the mobile network.</p></td>
</tr>
<tr class="odd">
<td><a href="element-networkconfiguration.md">NetworkConfiguration</a> </td>
<td><div class="alert">
<strong>Note</strong>  The <strong>NetworkConfiguration</strong> element is deprecated. Starting with Windows 8 and Windows Server 2012, the mobile operator should use Access Point Name (APN) Database to provide Purchase and Internet APN information.
</div>
<div>
 
</div>
<p>Defines the network configuration for the mobile broadband Purchase and Internet profiles to be used for mobile network.</p></td>
</tr>
<tr class="even">
<td><a href="element-provisioningengine.md">ProvisioningEngine</a> </td>
<td><p>Defines the trusted certificate values for Subject Name and Issuer Name required for provisioning on the mobile network.</p></td>
</tr>
<tr class="odd">
<td><a href="element-purchase.md">Purchase</a> </td>
<td><div class="alert">
<strong>Note</strong>  The <strong>Purchase</strong> element is deprecated. Starting with Windows 8 and Windows Server 2012, the mobile operator should use Access Point Name (APN) Database to provide Purchase APN information.
</div>
<div>
 
</div>
<p>Defines the mobile broadband Purchase profile to be used for the mobile network.</p></td>
</tr>
<tr class="even">
<td><a href="element-subjectname.md">SubjectName</a> </td>
<td><p>Defines the subject name of the trusted certificate.</p></td>
</tr>
<tr class="odd">
<td><a href="element-trustedcertificate.md">TrustedCertificate</a> </td>
<td><p>Defines the subject name and issuer name of a trusted certificate required for provisioning on the mobile network.</p></td>
</tr>
<tr class="even">
<td><a href="element-trustedcertificates.md">TrustedCertificates</a> </td>
<td><p>Defines the list of trusted security certificates required for provisioning on the mobile network.</p></td>
</tr>
</tbody>
</table>

 

The full Mobile Broadband Account Experience (MBAE) schema is below:

``` syntax
<?xml version="1.0" encoding ="utf-16" ?>
<xs:schema
    targetNamespace="http://schemas.microsoft.com/windows/2010/12/DeviceMetadata/MobileBroadbandInfo"
    xmlns:tns="http://schemas.microsoft.com/windows/2010/12/DeviceMetadata/MobileBroadbandInfo"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" blockDefault="#all">

  <xs:element name="MobileBroadbandInfo" type="tns:MobileBroadbandInfoType" />

  <xs:complexType name="MobileBroadbandInfoType">
    <xs:sequence>
      <xs:element name="NetworkConfiguration" type="tns:NetworkConfigType" minOccurs="0" />
      <xs:element name="ProvisioningEngine" type="tns:ProvisioningEngineType" minOccurs="0" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="NetworkConfigType">
    <xs:sequence>
      <xs:element name="MobileBroadbandProfiles" type="tns:MobileBroadbandProfilesType" minOccurs="0" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="MobileBroadbandProfilesType">
    <xs:sequence>
      <xs:element name="Purchase" type="tns:FileType" minOccurs="0" />
      <xs:element name="Internet" type="tns:FileType" minOccurs="0" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="FileType">
    <xs:restriction base="xs:string">
      <xs:whiteSpace value="preserve"/>
      <xs:pattern value="[\p{L}\p{N}\.\-_ ]+" />
      <xs:minLength value="1" />
      <xs:maxLength value="260" />
    </xs:restriction>
  </xs:simpleType>

  <xs:complexType name="ProvisioningEngineType">
    <xs:sequence>
      <xs:element name="TrustedCertificates" type="tns:TrustedCertificateListType" minOccurs="0" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="TrustedCertificateListType">
    <xs:sequence>
      <xs:element name="TrustedCertificate" type="tns:TrustedCertificateType"
                  minOccurs="0" maxOccurs="256" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="TrustedCertificateType">
    <xs:sequence>
      <xs:element name="SubjectName" type="xs:string" />
      <xs:element name="IssuerName" type="xs:string" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>

</xs:schema>
```

 

 



