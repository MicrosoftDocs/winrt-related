---
Description: The ResultsSchema schema defines elements that are returned from a call to ProvisionResultsXml and describe the results of the last provisioning attempt.
Search.Product: eADQiWindows 10XVcnh
title: ResultsSchema schema
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/2017
---

# ResultsSchema schema


The ResultsSchema schema defines elements that are returned from a call to [**ProvisionResultsXml**](https://msdn.microsoft.com/library/windows/apps/br212048) and describe the results of the last provisioning attempt. All of the elements are in the namespace http://www.microsoft.com/networking/CarrierControlResults/v1. Not all elements are in every profile, as some elements are optional.

The [ResultsSchema\_v2](https://msdn.microsoft.com/library/windows/apps/dn394062) schema defines additional elements in the *http://www.microsoft.com/networking/CarrierControlResults/v2* namespace and is supported on Windows 8.1, Windows Server 2012 R2, and later.

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
<td>[Activation](element-activation.md)</td>
<td><p>Contains any errors from processing the [<strong>Activation</strong>](https://msdn.microsoft.com/library/windows/apps/hh868285) element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td>[CarrierProvisioningResult](element-carrierprovisioningresult.md)</td>
<td><p>Contains any errors from processing the [<strong>CarrierProvisioning</strong>](https://msdn.microsoft.com/library/windows/apps/hh868289) element from the last provisioning attempt. [<strong>CarrierProvisioningResult</strong>](element-carrierprovisioningresult.md) is the unique root element for the provisioning results.</p></td>
</tr>
<tr class="odd">
<td>[DefaultProfile](element-defaultprofile.md)</td>
<td><p>Contains any errors from processing the [<strong>DefaultProfile</strong>](https://msdn.microsoft.com/library/windows/apps/hh868453) element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td>[Issuer](element-issuer.md)</td>
<td><p>Contains any errors from processing the [<strong>CarrierId</strong>](https://msdn.microsoft.com/library/windows/apps/hh868288) element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td>[MBNProfiles](element-mbnprofiles.md)</td>
<td><p>Contains any errors from processing the [<strong>MBNProfiles</strong>](https://msdn.microsoft.com/library/windows/apps/hh868295) element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td>[NotificationSignatureKey](element-notificationsignaturekey.md)</td>
<td><p>Contains any errors from processing the [<strong>KeyInfo</strong>](https://msdn.microsoft.com/library/windows/apps/hh868321) element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td>[Policy](element-policy.md)</td>
<td><p>Contains any errors from processing the [<strong>CarrierPolicy</strong>](https://msdn.microsoft.com/library/windows/apps/hh868345) schema from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td>[Provisioning](element-provisioning.md)</td>
<td><p>Contains any errors from processing the [<strong>Provisioning</strong>](https://msdn.microsoft.com/library/windows/apps/hh868300) element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td>[PurchaseProfile](element-purchaseprofile.md)</td>
<td><p>Contains any errors from processing the [<strong>PurchaseProfile</strong>](https://msdn.microsoft.com/library/windows/apps/hh868470) element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td>[RefreshParameters](element-refreshparameters.md)</td>
<td><p>Contains any errors from processing the [<strong>RefreshParameters</strong>](https://msdn.microsoft.com/library/windows/apps/hh868302) element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td>[Signature](element-signature.md)</td>
<td><p>Contains any errors from processing the [<strong>Signature</strong>](https://msdn.microsoft.com/library/windows/apps/hh868330) element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td>[Subject](element-subject.md)</td>
<td><p>Contains the X.509 certificate subject field of the [<strong>Signature</strong>](https://msdn.microsoft.com/library/windows/apps/hh868330) element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td>[Subscriber](element-subscriber.md)</td>
<td><p>Contains any errors from processing the [<strong>SubscriberId</strong>](https://msdn.microsoft.com/library/windows/apps/hh868305) element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td>[Thumbprint](element-thumbprint.md)</td>
<td><p>Contains the [<strong>SignatureValue</strong>](https://msdn.microsoft.com/library/windows/apps/hh868332) element of the [<strong>Signature</strong>](https://msdn.microsoft.com/library/windows/apps/hh868330) from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td>[TrustedCertificate](element-trustedcertificate.md)</td>
<td><p>Contains errors from processing any of the [<strong>TrustedCertificate</strong>](https://msdn.microsoft.com/library/windows/apps/hh868306) element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td>[WLANProfile](element-wlanprofile.md)</td>
<td><p>Contains any errors from processing a [<strong>WLANProfile</strong>](https://msdn.microsoft.com/library/windows/apps/hh868422) element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td>[WLANProfiles](element-wlanprofiles.md)</td>
<td><p>Contains any errors from processing the [<strong>WLANProfile</strong>](https://msdn.microsoft.com/library/windows/apps/hh868422) elements from the last provisioning attempt.</p></td>
</tr>
</tbody>
</table>

 

The full ResultsSchema schema is below:

``` syntax
<?xml version="1.0" encoding="utf-8"?>
<xs:schema targetNamespace="http://www.microsoft.com/networking/CarrierControlResults/v1"
    elementFormDefault="qualified"
    xmlns="http://www.microsoft.com/networking/CarrierControlResults/v1"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:prov="http://www.microsoft.com/networking/CarrierControl/v1">

  <xs:include schemaLocation="CarrierControlSchema.xsd"/>

  <xs:simpleType name="ErrorCodeType">
    <xs:restriction base="xs:token">
      <xs:pattern value="[0-9a-f]{8}"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:complexType name="AttemptedObject">
    <xs:attribute name="errorCode" type="ErrorCodeType" />
  </xs:complexType>

  <xs:complexType name="AttemptedLeafObject">
    <xs:attribute name="errorCode" type="ErrorCodeType" use="required"/>
  </xs:complexType>    

  <xs:element name="CarrierProvisioningResult">
    <xs:complexType>
      <xs:complexContent>
        <xs:extension base="AttemptedObject">
          <xs:all minOccurs="0">
            <!-- Carries the same information originally included in the file. -->
            <xs:element name="Issuer" type="prov:GUID"/>
            <xs:element name="Subscriber" type="prov:SubscriberType"/>

            <xs:element name="Activation" type="AttemptedLeafObject" minOccurs="0"/>

            <xs:element name="MBNProfiles" minOccurs="0">
              <xs:complexType>
                <xs:complexContent>
                  <xs:extension base="AttemptedObject">
                    <xs:sequence minOccurs="0">
                      <xs:element name="DefaultProfile" type="AttemptedLeafObject" minOccurs="0"/>
                      <xs:element name="PurchaseProfile" type="AttemptedLeafObject" minOccurs="0"/>
                    </xs:sequence>
                  </xs:extension>
                </xs:complexContent>
              </xs:complexType>
            </xs:element>

            <xs:element name="WLANProfiles" minOccurs="0">
              <xs:complexType>
                <xs:complexContent>
                  <xs:extension base="AttemptedObject">
                    <xs:sequence minOccurs="0">
                      <xs:element name="WLANProfile" maxOccurs="unbounded">
                        <xs:complexType>
                          <xs:complexContent>
                            <xs:extension base="AttemptedLeafObject">
                              <xs:attribute name="Name" use="required"/>
                            </xs:extension>
                          </xs:complexContent>
                        </xs:complexType>
                      </xs:element>
                    </xs:sequence>
                  </xs:extension>
                </xs:complexContent>
              </xs:complexType>
            </xs:element>

            <xs:element name="Provisioning" minOccurs="0">
              <xs:complexType>
                <xs:complexContent>
                  <xs:extension base="AttemptedObject">
                    <xs:sequence minOccurs="0">
                      <xs:element name="RefreshParameters" minOccurs="0">
                        <xs:complexType>
                          <xs:complexContent>
                            <xs:extension base="AttemptedLeafObject">
                              <xs:sequence minOccurs="0">
                                <xs:element name="NotificationSignatureKey" type="AttemptedLeafObject" minOccurs="0"/>
                              </xs:sequence>
                            </xs:extension>
                          </xs:complexContent>
                        </xs:complexType>
                      </xs:element>
                      <xs:element name="TrustedCertificate" type="AttemptedLeafObject" minOccurs="0"/>
                      <xs:element name="Policy" type="AttemptedLeafObject" minOccurs="0"/>
                    </xs:sequence>
                  </xs:extension>
                </xs:complexContent>
              </xs:complexType>
            </xs:element>

            <xs:element name="Signature">
              <xs:complexType>
                <xs:complexContent>
                  <xs:extension base="AttemptedLeafObject">
                    <xs:sequence minOccurs="0">
                      <xs:element name="Subject" type="xs:string"/>
                      <xs:element name="Thumbprint" type="xs:base64Binary"/>
                    </xs:sequence>
                  </xs:extension>
                </xs:complexContent>
              </xs:complexType>
            </xs:element>

          </xs:all>
        </xs:extension>
      </xs:complexContent>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

## Related topics


[ResultsSchema\_v2 schema](https://msdn.microsoft.com/library/windows/apps/dn394062)

 

 



