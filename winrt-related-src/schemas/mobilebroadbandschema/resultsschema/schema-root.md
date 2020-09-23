---
Description: The ResultsSchema schema defines elements that are returned from a call to ProvisionResultsXml and describe the results of the last provisioning attempt.
Search.Product: eADQiWindows 10XVcnh
title: ResultsSchema schema
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# ResultsSchema schema


The ResultsSchema schema defines elements that are returned from a call to [**ProvisionResultsXml**](/uwp/api/Windows.Networking.NetworkOperators.ProvisionFromXmlDocumentResults) and describe the results of the last provisioning attempt. All of the elements are in the namespace `http://www.microsoft.com/networking/CarrierControlResults/v1`. Not all elements are in every profile, as some elements are optional.

The [ResultsSchema\_v2](../resultsschema-v2/schema-root.md) schema defines additional elements in the `http://www.microsoft.com/networking/CarrierControlResults/v2` namespace and is supported on Windows 8.1, Windows Server 2012 R2, and later.

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
<td><a href="element-activation.md">Activation</a> </td>
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolschema/element-activation"><strong>Activation</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td><a href="element-carrierprovisioningresult.md">CarrierProvisioningResult</a> </td>
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolschema/element-carrierprovisioning"><strong>CarrierProvisioning</strong></a>  element from the last provisioning attempt. <a href="element-carrierprovisioningresult.md"><strong>CarrierProvisioningResult</strong></a> is the unique root element for the provisioning results.</p></td>
</tr>
<tr class="odd">
<td><a href="element-defaultprofile.md">DefaultProfile</a> </td>
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/wwan/element-defaultprofile"><strong>DefaultProfile</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td><a href="element-issuer.md">Issuer</a> </td>
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolschema/element-carrierid"><strong>CarrierId</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td><a href="element-mbnprofiles.md">MBNProfiles</a> </td>
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolschema/element-mbnprofiles"><strong>MBNProfiles</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td><a href="element-notificationsignaturekey.md">NotificationSignatureKey</a> </td>
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolsignatureschema/element-keyinfo"><strong>KeyInfo</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td><a href="element-policy.md">Policy</a> </td>
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/dusm/element-carrierpolicy"><strong>CarrierPolicy</strong></a>  schema from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td><a href="element-provisioning.md">Provisioning</a> </td>
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolschema/element-provisioning"><strong>Provisioning</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td><a href="element-purchaseprofile.md">PurchaseProfile</a> </td>
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/wwan/element-purchaseprofile"><strong>PurchaseProfile</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td><a href="element-refreshparameters.md">RefreshParameters</a> </td>
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolschema/element-refreshparameters"><strong>RefreshParameters</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td><a href="element-signature.md">Signature</a> </td>
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolsignatureschema/element-signature"><strong>Signature</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td><a href="element-subject.md">Subject</a> </td>
<td><p>Contains the X.509 certificate subject field of the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolsignatureschema/element-signature"><strong>Signature</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td><a href="element-subscriber.md">Subscriber</a> </td>
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolschema/element-subscriberid"><strong>SubscriberId</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td><a href="element-thumbprint.md">Thumbprint</a> </td>
<td><p>Contains the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolsignatureschema/element-signaturevalue"><strong>SignatureValue</strong></a>  element of the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolsignatureschema/element-signature"><strong>Signature</strong></a> from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td><a href="element-trustedcertificate.md">TrustedCertificate</a> </td>
<td><p>Contains errors from processing any of the <a href="/uwp/schemas/mobilebroadbandschema/carriercontrolschema/element-trustedcertificate"><strong>TrustedCertificate</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td><a href="element-wlanprofile.md">WLANProfile</a> </td>
<td><p>Contains any errors from processing a <a href="/uwp/schemas/mobilebroadbandschema/wlan/element-wlanprofile"><strong>WLANProfile</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td><a href="element-wlanprofiles.md">WLANProfiles</a> </td>
<td><p>Contains any errors from processing the <a href="/uwp/schemas/mobilebroadbandschema/wlan/element-wlanprofile"><strong>WLANProfile</strong></a>  elements from the last provisioning attempt.</p></td>
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


[ResultsSchema\_v2 schema](../resultsschema-v2/schema-root.md)

 

 