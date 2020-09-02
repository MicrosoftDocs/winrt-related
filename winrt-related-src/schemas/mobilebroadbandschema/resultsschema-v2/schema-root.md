---
Description: The ResultsSchema\_v2 schema defines additional elements that are returned from a call to ProvisionResultsXml and describe the results of the last provisioning attempt.
Search.Product: eADQiWindows 10XVcnh
title: ResultsSchema\_v2 schema
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# ResultsSchema\_v2 schema


The ResultsSchema\_v2 schema defines additional elements that are returned from a call to [**ProvisionResultsXml**](/uwp/api/Windows.Networking.NetworkOperators.ProvisionFromXmlDocumentResults) and describe the results of the last provisioning attempt. All of the elements are in the namespace `http://www.microsoft.com/networking/CarrierControlResults/v2`. Not all elements are in every profile, as some elements are optional.

The ResultsSchema\_v2 schema elements are additions to the [ResultsSchema](../resultsschema/schema-root.md) version 1 schema defined in the `http://www.microsoft.com/networking/CarrierControlResults/v1` namespace.

The ResultsSchema\_v2 schema is supported on Windows 8.1, Windows Server 2012 R2, and later.

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
<td><p>Contains any errors from processing the <a href="https://msdn.microsoft.com/library/windows/apps/hh868285"><strong>Activation</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td><a href="element-additionalpdpcontexts.md">AdditionalPDPContexts</a> </td>
<td><p>Contains any errors from processing the <a href="https://msdn.microsoft.com/library/windows/apps/dn393994"><strong>AdditionalPDPContexts</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td><a href="element-carriernetworkmetadata.md">CarrierNetworkMetadata</a> </td>
<td><p>Contains any errors from processing the <a href="https://msdn.microsoft.com/library/windows/apps/dn393998"><strong>CarrierNetworkMetadata</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td><a href="element-carrierprovisioningresult.md">CarrierProvisioningResult</a> </td>
<td><p>Contains any errors from processing the <a href="https://msdn.microsoft.com/library/windows/apps/hh868289"><strong>CarrierProvisioning</strong></a>  element from the last provisioning attempt. <a href="https://msdn.microsoft.com/library/windows/apps/hh868380"><strong>CarrierProvisioningResult</strong></a> is the unique root element for the provisioning results.</p></td>
</tr>
<tr class="odd">
<td><a href="element-customersupportphonenumber.md">CustomerSupportPhoneNumber</a> </td>
<td><p>Contains any errors from processing the <a href="https://msdn.microsoft.com/library/windows/apps/dn394004"><strong>CustomerSupportPhoneNumber</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td><a href="element-dataclassfriendlynames.md">DataClassFriendlyNames</a> </td>
<td><p>Contains any errors from processing the <a href="https://msdn.microsoft.com/library/windows/apps/dn394005"><strong>DataClassFriendlyNames</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td><a href="element-defaultprofile.md">DefaultProfile</a> </td>
<td><p>Contains any errors from processing the <a href="https://msdn.microsoft.com/library/windows/apps/hh868453"><strong>DefaultProfile</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td><a href="element-issuer.md">Issuer</a> </td>
<td><p>Contains any errors from processing the <a href="https://msdn.microsoft.com/library/windows/apps/hh868288"><strong>CarrierId</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td><a href="element-mbnprofiles.md">MBNProfiles</a> </td>
<td><p>Contains any errors from processing the <a href="https://msdn.microsoft.com/library/windows/apps/hh868295"><strong>MBNProfiles</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td><a href="element-multiplepdpcontextpolicies.md">MultiplePDPContextPolicies</a> </td>
<td><p>Contains any errors from processing the <a href="https://msdn.microsoft.com/library/windows/apps/dn394018"><strong>MultiplePDPContextPolicies</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td><a href="element-networksettings.md">NetworkSettings</a> </td>
<td><p>Contains any errors from processing the <a href="https://msdn.microsoft.com/library/windows/apps/dn394020"><strong>NetworkSettings</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td><a href="element-pdpcontextpolicy.md">PDPContextPolicy</a> </td>
<td><p>Contains any errors from processing a <a href="https://msdn.microsoft.com/library/windows/apps/dn394028"><strong>PDPContextPolicy</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td><a href="element-plan.md">Plan</a> </td>
<td><p>Contains any errors from processing a <a href="https://msdn.microsoft.com/library/windows/apps/hh868298"><strong>Plan</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td><a href="element-plans.md">Plans</a> </td>
<td><p>Contains any errors from processing the <a href="https://msdn.microsoft.com/library/windows/apps/hh868299"><strong>Plans</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td><a href="element-provisioning.md">Provisioning</a> </td>
<td><p>Contains any errors from processing the <a href="https://msdn.microsoft.com/library/windows/apps/hh868300"><strong>Provisioning</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td><a href="element-purchaseprofile.md">PurchaseProfile</a> </td>
<td><p>Contains any errors from processing the <a href="https://msdn.microsoft.com/library/windows/apps/hh868470"><strong>PurchaseProfile</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td><a href="element-refreshparameters.md">RefreshParameters</a> </td>
<td><p>Contains any errors from processing the <a href="https://msdn.microsoft.com/library/windows/apps/hh868302"><strong>RefreshParameters</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td><a href="element-subscriber.md">Subscriber</a> </td>
<td><p>Contains any errors from processing the <a href="https://msdn.microsoft.com/library/windows/apps/hh868305"><strong>SubscriberId</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td><a href="element-tetheringprofile.md">TetheringProfile</a> </td>
<td><p>Contains any errors from processing a <a href="https://msdn.microsoft.com/library/windows/apps/dn394029"><strong>TetheringProfile</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td><a href="element-tetheringsettings.md">TetheringSettings</a> </td>
<td><p>Contains any errors from processing the <a href="https://msdn.microsoft.com/library/windows/apps/dn394030"><strong>TetheringSettings</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td><a href="element-trustedcertificate.md">TrustedCertificate</a> </td>
<td><p>Contains errors from processing any of the <a href="https://msdn.microsoft.com/library/windows/apps/hh868306"><strong>TrustedCertificate</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="even">
<td><a href="element-wlanprofile.md">WLANProfile</a> </td>
<td><p>Contains any errors from processing a <a href="https://msdn.microsoft.com/library/windows/apps/hh868422"><strong>WLANProfile</strong></a>  element from the last provisioning attempt.</p></td>
</tr>
<tr class="odd">
<td><a href="element-wlanprofiles.md">WLANProfiles</a> </td>
<td><p>Contains any errors from processing the <a href="https://msdn.microsoft.com/library/windows/apps/hh868422"><strong>WLANProfile</strong></a>  elements from the last provisioning attempt.</p></td>
</tr>
</tbody>
</table>

 

The full ResultsSchema\_v2 schema is below:

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


[ResultsSchema schema](../resultsschema/schema-root.md)

 

 