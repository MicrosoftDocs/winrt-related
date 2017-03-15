---
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c
author: mcleblanc
ms.author: markl
keywords: windows 10
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
<td>[Activation](element-activation.md)</td>
<td><p>Defines information for a subscriber's activation method on a Mobile Network Operator's (MNO) network.</p></td>
</tr>
<tr class="even">
<td>[ActivationMethod](element-activationmethod.md)</td>
<td><p>Defines an instance of the [<strong>ActivationMethod</strong>](https://msdn.microsoft.com/library/windows/apps/hh868442) element from the [<strong>WWAN</strong>](https://msdn.microsoft.com/library/windows/apps/hh868486) schema.</p></td>
</tr>
<tr class="odd">
<td>[Branding](element-branding.md)</td>
<td><p>Defines an instance of the [<strong>Branding</strong>](https://msdn.microsoft.com/library/windows/apps/hh868446) element from the [<strong>WWAN</strong>](https://msdn.microsoft.com/library/windows/apps/hh868486) schema.</p></td>
</tr>
<tr class="even">
<td>[CarrierId](element-carrierid.md)</td>
<td><p>Defines a unique GUID that identifies the Mobile Network Operator (MNO). If the MNO participates in MBAE, this should be their MBAE Carrier ID. Non-MBAE MNOs may generate a GUID as part of their initial configuration.</p></td>
</tr>
<tr class="odd">
<td>[CarrierProvisioning](element-carrierprovisioning.md)</td>
<td><p>Defines the properties and settings in a subscriber's carrier provisioning file. [<strong>CarrierProvisioning</strong>](element-carrierprovisioning.md) is the unique root element of the provisioning file.</p></td>
</tr>
<tr class="even">
<td>[DefaultProfile](element-defaultprofile.md)</td>
<td><p>Defines an instance of the [<strong>DefaultProfile</strong>](https://msdn.microsoft.com/library/windows/apps/hh868453) element from the [<strong>WWAN</strong>](https://msdn.microsoft.com/library/windows/apps/hh868486) schema.</p></td>
</tr>
<tr class="odd">
<td>[DelayInDays](element-delayindays.md)</td>
<td><p>Defines the number of days until the next refresh. It must be a positive integer less than 732.</p></td>
</tr>
<tr class="even">
<td>[DeviceId](element-deviceid.md)</td>
<td><p>Defines a unique device identifier to which this provisioning attempt applies. It must be formatted as <strong>\d{15,16}</strong> or as <strong>([a-fA-F0-9]{2}:){5}[a-fA-F0-9]{2}</strong></p></td>
</tr>
<tr class="odd">
<td>[Extensions](element-extensions.md)</td>
<td><p>Defines a schema extension point container for future additions.</p></td>
</tr>
<tr class="even">
<td>[Global](element-global.md)</td>
<td><p>Defines identifying information for this provisioning attempt on a Mobile Network Operator's (MNO) network.</p></td>
</tr>
<tr class="odd">
<td>[MBNProfiles](element-mbnprofiles.md)</td>
<td><p>Defines information for a subscriber's WWAN profiles on a Mobile Network Operator's (MNO) network.</p></td>
</tr>
<tr class="even">
<td>[Messages](element-messages.md)</td>
<td><p>Defines an instance of the [<strong>Messages</strong>](https://msdn.microsoft.com/library/windows/apps/hh868462) element from the [<strong>WWAN</strong>](https://msdn.microsoft.com/library/windows/apps/hh868486) schema.</p></td>
</tr>
<tr class="odd">
<td>[Password](element-password.md)</td>
<td><p>Defines optional password credentials to be presented using HTTP-Auth to log on to the Mobile Network Operator's network when retrieving the provisioning file.</p></td>
</tr>
<tr class="even">
<td>[Plan](element-plan.md)</td>
<td><p>Defines an instance of the [<strong>Plan</strong>](https://msdn.microsoft.com/library/windows/apps/hh868373) element from the [<strong>Plans</strong>](https://msdn.microsoft.com/library/windows/apps/hh868378) schema.</p></td>
</tr>
<tr class="odd">
<td>[Plans](element-plans.md)</td>
<td><p>Defines information for a subscriber's connection plans to a Mobile Network Operator's (MNO) network.</p></td>
</tr>
<tr class="even">
<td>[Provisioning](element-provisioning.md)</td>
<td><p>Defines parameters used to establish trust and refresh settings for future provisioning attempts.</p></td>
</tr>
<tr class="odd">
<td>[PurchaseProfile](element-purchaseprofile.md)</td>
<td><p>Defines an instance of the [<strong>PurchaseProfile</strong>](https://msdn.microsoft.com/library/windows/apps/hh868470) element from the [<strong>WWAN</strong>](https://msdn.microsoft.com/library/windows/apps/hh868486) schema.</p></td>
</tr>
<tr class="even">
<td>[RefreshParameters](element-refreshparameters.md)</td>
<td><p>Defines parameters to be used when refreshing the provisioning file contents.</p></td>
</tr>
<tr class="odd">
<td>[RefreshURL](element-refreshurl.md)</td>
<td><p>Defines the HTTPS URL where the client can find the updated copy of this provisioning file in the future. This URL will be accessed upon receipt of an SMS/USSD trigger or after the specified [<strong>DelayInDays</strong>](element-delayindays.md). It must be formatted as <strong>https://.+</strong></p></td>
</tr>
<tr class="even">
<td>[Signature](element-signature.md)</td>
<td><p>Defines an instance of the [<strong>Signature</strong>](https://msdn.microsoft.com/library/windows/apps/hh868330) element from the [<strong>CarrierControlSignatureSchema</strong>](https://msdn.microsoft.com/library/windows/apps/hh868341).</p></td>
</tr>
<tr class="odd">
<td>[SubscriberId](element-subscriberid.md)</td>
<td><p>Defines a unique subscriber account identifier to which this provisioning attempt applies.</p></td>
</tr>
<tr class="even">
<td>[TrustedCertificate](element-trustedcertificate.md)</td>
<td><p>Defines the Subject and Issuer fields from a trustworthy X.509 certificate.</p></td>
</tr>
<tr class="odd">
<td>[TrustedCertificates](element-trustedcertificates.md)</td>
<td><p>Defines a list of X.509 certificates whose signatures should be trusted on future provisioning files.</p></td>
</tr>
<tr class="even">
<td>[UserName](element-username.md)</td>
<td><p>Defines optional user name credentials to be presented using HTTP-Auth to log on to the Mobile Network Operator's network when retrieving the provisioning file.</p></td>
</tr>
<tr class="odd">
<td>[WLANProfile](element-wlanprofile.md)</td>
<td><p>Defines an instance of the [<strong>WLANProfile</strong>](https://msdn.microsoft.com/library/windows/apps/hh868422) element from the [<strong>WLAN</strong>](https://msdn.microsoft.com/library/windows/apps/hh868424) schema.</p></td>
</tr>
<tr class="even">
<td>[WLANProfiles](element-wlanprofiles.md)</td>
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

 

 



