---
title: CarrierControlSchema schema
description: The CarrierControlSchema schema defines elements that are used to create the provisioning file in a call to ProvisionFromXmlDocumentAsync and describe all of the settings required to authenticate and provision a subscriber's account on a Mobile Network Operator's (MNO) network.
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# CarrierControlSchema schema


The CarrierControlSchema schema defines elements that are used to create the provisioning file in a call to [**ProvisionFromXmlDocumentAsync**](https://msdn.microsoft.com/library/windows/apps/br207400) and describe all of the settings required to authenticate and provision a subscriber's account on a Mobile Network Operator's (MNO) network. All of the elements are in the namespace http://www.microsoft.com/networking/CarrierControl/v1. Not all elements are in every profile, as some elements are optional.

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
<td><p>Defines information for a subscriber's activation method on a Mobile Network Operator's (MNO) network.</p></td>
</tr>
<tr class="even">
<td><a href="element-activationmethod.md">ActivationMethod</a> </td>
<td><p>Defines an instance of the <a href="https://msdn.microsoft.com/library/windows/apps/hh868442"><strong>ActivationMethod</strong></a>  element from the <a href="https://msdn.microsoft.com/library/windows/apps/hh868486"><strong>WWAN</strong></a> schema.</p></td>
</tr>
<tr class="odd">
<td><a href="element-branding.md">Branding</a> </td>
<td><p>Defines an instance of the <a href="https://msdn.microsoft.com/library/windows/apps/hh868446"><strong>Branding</strong></a>  element from the <a href="https://msdn.microsoft.com/library/windows/apps/hh868486"><strong>WWAN</strong></a> schema.</p></td>
</tr>
<tr class="even">
<td><a href="element-carrierid.md">CarrierId</a> </td>
<td><p>Defines a unique GUID that identifies the Mobile Network Operator (MNO). If the MNO participates in MBAE, this should be their MBAE Carrier ID. Non-MBAE MNOs may generate a GUID as part of their initial configuration.</p></td>
</tr>
<tr class="odd">
<td><a href="element-carrierprovisioning.md">CarrierProvisioning</a> </td>
<td><p>Defines the properties and settings in a subscriber's carrier provisioning file. <a href="element-carrierprovisioning.md"><strong>CarrierProvisioning</strong></a>  is the unique root element of the provisioning file.</p></td>
</tr>
<tr class="even">
<td><a href="element-defaultprofile.md">DefaultProfile</a> </td>
<td><p>Defines an instance of the <a href="https://msdn.microsoft.com/library/windows/apps/hh868453"><strong>DefaultProfile</strong></a>  element from the <a href="https://msdn.microsoft.com/library/windows/apps/hh868486"><strong>WWAN</strong></a> schema.</p></td>
</tr>
<tr class="odd">
<td><a href="element-delayindays.md">DelayInDays</a> </td>
<td><p>Defines the number of days until the next refresh. It must be a positive integer less than 732.</p></td>
</tr>
<tr class="even">
<td><a href="element-deviceid.md">DeviceId</a> </td>
<td><p>Defines a unique device identifier to which this provisioning attempt applies. It must be formatted as <strong>\d{15,16}</strong> or as <strong>([a-fA-F0-9]{2}:){5}[a-fA-F0-9]{2}</strong></p></td>
</tr>
<tr class="odd">
<td><a href="element-extensions.md">Extensions</a> </td>
<td><p>Defines a schema extension point container for future additions.</p></td>
</tr>
<tr class="even">
<td><a href="element-global.md">Global</a> </td>
<td><p>Defines identifying information for this provisioning attempt on a Mobile Network Operator's (MNO) network.</p></td>
</tr>
<tr class="odd">
<td><a href="element-mbnprofiles.md">MBNProfiles</a> </td>
<td><p>Defines information for a subscriber's WWAN profiles on a Mobile Network Operator's (MNO) network.</p></td>
</tr>
<tr class="even">
<td><a href="element-messages.md">Messages</a> </td>
<td><p>Defines an instance of the <a href="https://msdn.microsoft.com/library/windows/apps/hh868462"><strong>Messages</strong></a>  element from the <a href="https://msdn.microsoft.com/library/windows/apps/hh868486"><strong>WWAN</strong></a> schema.</p></td>
</tr>
<tr class="odd">
<td><a href="element-password.md">Password</a> </td>
<td><p>Defines optional password credentials to be presented using HTTP-Auth to log on to the Mobile Network Operator's network when retrieving the provisioning file.</p></td>
</tr>
<tr class="even">
<td><a href="element-plan.md">Plan</a> </td>
<td><p>Defines an instance of the <a href="https://msdn.microsoft.com/library/windows/apps/hh868373"><strong>Plan</strong></a>  element from the <a href="https://msdn.microsoft.com/library/windows/apps/hh868378"><strong>Plans</strong></a> schema.</p></td>
</tr>
<tr class="odd">
<td><a href="element-plans.md">Plans</a> </td>
<td><p>Defines information for a subscriber's connection plans to a Mobile Network Operator's (MNO) network.</p></td>
</tr>
<tr class="even">
<td><a href="element-provisioning.md">Provisioning</a> </td>
<td><p>Defines parameters used to establish trust and refresh settings for future provisioning attempts.</p></td>
</tr>
<tr class="odd">
<td><a href="element-purchaseprofile.md">PurchaseProfile</a> </td>
<td><p>Defines an instance of the <a href="https://msdn.microsoft.com/library/windows/apps/hh868470"><strong>PurchaseProfile</strong></a>  element from the <a href="https://msdn.microsoft.com/library/windows/apps/hh868486"><strong>WWAN</strong></a> schema.</p></td>
</tr>
<tr class="even">
<td><a href="element-refreshparameters.md">RefreshParameters</a> </td>
<td><p>Defines parameters to be used when refreshing the provisioning file contents.</p></td>
</tr>
<tr class="odd">
<td><a href="element-refreshurl.md">RefreshURL</a> </td>
<td><p>Defines the HTTPS URL where the client can find the updated copy of this provisioning file in the future. This URL will be accessed upon receipt of an SMS/USSD trigger or after the specified <a href="element-delayindays.md"><strong>DelayInDays</strong></a> . It must be formatted as <strong>https://.+</strong></p></td>
</tr>
<tr class="even">
<td><a href="element-signature.md">Signature</a> </td>
<td><p>Defines an instance of the <a href="https://msdn.microsoft.com/library/windows/apps/hh868330"><strong>Signature</strong></a>  element from the <a href="https://msdn.microsoft.com/library/windows/apps/hh868341"><strong>CarrierControlSignatureSchema</strong></a>.</p></td>
</tr>
<tr class="odd">
<td><a href="element-subscriberid.md">SubscriberId</a> </td>
<td><p>Defines a unique subscriber account identifier to which this provisioning attempt applies.</p></td>
</tr>
<tr class="even">
<td><a href="element-trustedcertificate.md">TrustedCertificate</a> </td>
<td><p>Defines the Subject and Issuer fields from a trustworthy X.509 certificate.</p></td>
</tr>
<tr class="odd">
<td><a href="element-trustedcertificates.md">TrustedCertificates</a> </td>
<td><p>Defines a list of X.509 certificates whose signatures should be trusted on future provisioning files.</p></td>
</tr>
<tr class="even">
<td><a href="element-username.md">UserName</a> </td>
<td><p>Defines optional user name credentials to be presented using HTTP-Auth to log on to the Mobile Network Operator's network when retrieving the provisioning file.</p></td>
</tr>
<tr class="odd">
<td><a href="element-wlanprofile.md">WLANProfile</a> </td>
<td><p>Defines an instance of the <a href="https://msdn.microsoft.com/library/windows/apps/hh868422"><strong>WLANProfile</strong></a>  element from the <a href="https://msdn.microsoft.com/library/windows/apps/hh868424"><strong>WLAN</strong></a> schema.</p></td>
</tr>
<tr class="even">
<td><a href="element-wlanprofiles.md">WLANProfiles</a> </td>
<td><p>Defines information for a subscriber's WLAN profiles on a Mobile Network Operator's (MNO) network.</p></td>
</tr>
</tbody>
</table>

 

The full CarrierControlSchema schema is below:

``` syntax
<?xml version="1.0" encoding="utf-8"?>  
<xs:schema targetNamespace="http://www.microsoft.com/networking/CarrierControl/v1"  
    elementFormDefault="qualified"  
    xmlns="http://www.microsoft.com/networking/CarrierControl/v1"  
    xmlns:xs="http://www.w3.org/2001/XMLSchema"  
    xmlns:ds="http://www.w3.org/2000/09/xmldsig#"  
    xmlns:wwan="http://www.microsoft.com/networking/CarrierControl/WWAN/v1"  
    xmlns:wlan="http://www.microsoft.com/networking/CarrierControl/WLAN/v1"  
    xmlns:base="http://www.microsoft.com/networking/CarrierControl/Base/v1"  
    xmlns:plans="http://www.microsoft.com/networking/CarrierControl/Plans/v1">  
  
  <xs:import namespace="http://www.microsoft.com/networking/CarrierControl/WLAN/v1" />  
  <xs:import namespace="http://www.microsoft.com/networking/CarrierControl/WWAN/v1" />  
  <xs:import namespace="http://www.microsoft.com/networking/CarrierControl/Base/v1" />  
  <xs:import namespace="http://www.microsoft.com/networking/CarrierControl/Plans/v1" />  
  <xs:import namespace="http://www.w3.org/2000/09/xmldsig#" />  
  
  <xs:element name="CarrierProvisioning">  
    <xs:complexType>  
      <xs:sequence>  
  
        <xs:element name="Global">  
          <xs:complexType>  
            <xs:sequence>  
              <xs:element name="CarrierId" type="base:GUID"/>  
              <xs:element name="SubscriberId" type="base:SubscriberType"/>  
              <xs:element name="DeviceId" minOccurs="0">  
                <xs:simpleType>  
                  <xs:restriction base="xs:token">  
                    <xs:pattern value="\d{15,16}"/>  
                    <xs:pattern value="([a-fA-F0-9]{2}:){5}[a-fA-F0-9]{2}"/>  
                  </xs:restriction>  
                </xs:simpleType>  
              </xs:element>  
  
              <xs:any minOccurs="0" maxOccurs="unbounded" namespace="##other"/>  
            </xs:sequence>  
          </xs:complexType>  
        </xs:element>  
  
        <xs:element name="Activation" minOccurs="0">  
          <xs:complexType>  
            <xs:sequence>  
              <xs:element ref="wwan:ActivationMethod"/>
            </xs:sequence>  
          </xs:complexType>  
        </xs:element>  
        <xs:element name="MBNProfiles" minOccurs="0">  
          <xs:complexType>  
            <xs:sequence>  
              <xs:element ref="wwan:DefaultProfile" minOccurs="0"/>  
              <xs:element ref="wwan:PurchaseProfile" minOccurs="0"/>  
              <xs:element ref="wwan:Messages" minOccurs="0"/>  
              <xs:element ref="wwan:Branding" minOccurs="0"/>
            </xs:sequence>  
          </xs:complexType>  
        </xs:element>  

        <xs:element name="WLANProfiles" minOccurs="0">  
          <xs:complexType>  
            <xs:sequence>  
              <xs:element ref="wlan:WLANProfile" maxOccurs="unbounded" minOccurs="0"/>
            </xs:sequence>  
          </xs:complexType>  
        </xs:element>  
 
        <xs:element name="Plans" minOccurs="0">  
          <xs:complexType>  
            <xs:sequence>  
              <xs:element ref="plans:Plan" maxOccurs="unbounded"/>
            </xs:sequence>  
          </xs:complexType>  
        </xs:element>  

        <xs:element name="Provisioning" minOccurs="0">  
          <xs:complexType>  
            <xs:sequence>  
              <xs:element name="TrustedCertificates" minOccurs="0">  
                <xs:complexType>    
                  <xs:sequence>  
                    <xs:element name="TrustedCertificate" type="base:CertificateDetails" maxOccurs="unbounded"/>  
                  </xs:sequence>  
                </xs:complexType>  
              </xs:element>
  
              <xs:element name="RefreshParameters" minOccurs="0">  
                <xs:complexType>  
                  <xs:sequence>  
                    <xs:element name="DelayInDays" minOccurs="0">  
                      <xs:simpleType>  
                        <xs:restriction base="xs:positiveInteger">  
                          <xs:maxExclusive value="731"/>  
                        </xs:restriction>  
                      </xs:simpleType>  
                    </xs:element>  
  
                    <xs:element name="RefreshURL">  
                      <xs:simpleType>  
                        <xs:restriction base="xs:anyURI">  
                          <xs:pattern value="https://.+"/>  
                        </xs:restriction>  
                      </xs:simpleType>  
                    </xs:element>  
  
                    <xs:element name="UserName" type="xs:token" minOccurs="0"/>  
                    <xs:element name="Password" type="xs:token" minOccurs="0"/>  
  
                  </xs:sequence>  
                </xs:complexType>  
              </xs:element>  
            </xs:sequence>  
          </xs:complexType>  
        </xs:element>  

        <xs:element name="Extensions" minOccurs="0">  
          <xs:complexType>  
            <xs:sequence>  
              <xs:any minOccurs="0" maxOccurs="unbounded" namespace="##other"/>  
            </xs:sequence>  
          </xs:complexType>  
        </xs:element>
          
        <xs:element ref="ds:Signature" minOccurs="0"/>          
      </xs:sequence>  
    </xs:complexType>  
  </xs:element>  
</xs:schema>
```

 

 



