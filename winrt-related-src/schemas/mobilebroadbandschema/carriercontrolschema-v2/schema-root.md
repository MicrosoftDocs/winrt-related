---
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c
author: mcleblanc
ms.author: markl
keywords: windows 10
---

# CarrierControlSchema\_v2 schema


The CarrierControlSchema\_v2 schema defines additional elements that are used to create the provisioning file in a call to [**ProvisionFromXmlDocumentAsync**](https://msdn.microsoft.com/library/windows/apps/br207400) and describe additional settings required to authenticate and provision a subscriber's account on a Mobile Network Operator's (MNO) network. All of the elements are in the namespace http://www.microsoft.com/networking/CarrierControl/v2. Not all elements are in every profile, as some elements are optional.

The CarrierControlSchema\_v2 schema elements are additions to the [CarrierControlSchema](https://msdn.microsoft.com/library/windows/apps/hh868312) version 1 schema defined in the http://www.microsoft.com/networking/CarrierControl/v1 namespace.

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
<td>[AccessString](element-accessstring.md)</td>
<td><p>Defines the access string for a context in the Packet Data Protocol (PDP) context policy.</p></td>
</tr>
<tr class="even">
<td>[AdditionalPDPContexts](element-additionalpdpcontexts.md)</td>
<td><p>Defines additional Packet Data Protocol (PDP) contexts in a subscriber's carrier provisioning file.</p></td>
</tr>
<tr class="odd">
<td>[AppID](element-appid.md)</td>
<td><p>Defines the application ID used for Packet Data Protocol (PDP) context allowed list.</p></td>
</tr>
<tr class="even">
<td>[AppIDList](element-appidlist.md)</td>
<td><p>Defines the list of applications that are part of the Packet Data Protocol (PDP) context allowed list.</p></td>
</tr>
<tr class="odd">
<td>[AuthProtocol](element-authprotocol.md)</td>
<td><p>Defines the authentication protocol to use for a context in the Packet Data Protocol (PDP) context policy.</p></td>
</tr>
<tr class="even">
<td>[CUSTOM](element-custom.md)</td>
<td><p>Defines a custom protocol used for mobile network data.</p></td>
</tr>
<tr class="odd">
<td>[CarrierNetworkMetadata](element-carriernetworkmetadata.md)</td>
<td><p>Defines the network properties and settings in a subscriber's carrier provisioning file.</p></td>
</tr>
<tr class="even">
<td>[Compression](element-compression.md)</td>
<td><p>Defines whether compression is enabled for a context in the Packet Data Protocol (PDP) context policy.</p></td>
</tr>
<tr class="odd">
<td>[Context](element-context.md)</td>
<td><p>Defines the context of a Packet Data Protocol (PDP) context policy in a subscriber's carrier provisioning file.</p></td>
</tr>
<tr class="even">
<td>[CustomerSupportPhoneNumber](element-customersupportphonenumber.md)</td>
<td><p>Defines the phone number for customer support in a subscriber's carrier provisioning file.</p></td>
</tr>
<tr class="odd">
<td>[DNSRetryCount](element-dnsretrycount.md)</td>
<td><p>Defines the DNS retry count. It must be a positive integer between 1 and 4.</p></td>
</tr>
<tr class="even">
<td>[DNSRetryIntervalInSeconds](element-dnsretryintervalinseconds.md)</td>
<td><p>Defines the DNS retry interval in seconds. It must be a positive integer between 1 and 4.</p></td>
</tr>
<tr class="odd">
<td>[DNSRetrySettings](element-dnsretrysettings.md)</td>
<td><p>Defines the network settings for DNS retries in a subscriber's carrier provisioning file.</p></td>
</tr>
<tr class="even">
<td>[DataClassFriendlyNames](element-dataclassfriendlynames.md)</td>
<td><p>Defines class friendly names for the standard or protocol used for mobile network data in a subscriber's carrier provisioning file.</p></td>
</tr>
<tr class="odd">
<td>[EDGE](element-edge.md)</td>
<td><p>Defines the Enhanced Data rates for the GSM Evolution (EDGE) protocol used for mobile network data.</p></td>
</tr>
<tr class="even">
<td>[Extensions_v2](element-extensions-v2.md)</td>
<td><p>Defines additional properties and settings in a subscriber's carrier provisioning file. [<strong>Extensions_v2</strong>](element-extensions-v2.md) is the unique root element of the [CarrierControlSchema_v2](schema-root.md) provisioning file.</p></td>
</tr>
<tr class="odd">
<td>[GPRS](element-gprs.md)</td>
<td><p>Defines the general packet radio service (GPRS) protocol used for mobile network data.</p></td>
</tr>
<tr class="even">
<td>[HSDPA](element-hsdpa.md)</td>
<td><p>Defines the High-Speed Downlink Packet Access (HSDPA) protocol used for mobile network data.</p></td>
</tr>
<tr class="odd">
<td>[HSUPA](element-hsupa.md)</td>
<td><p>Defines the High-Speed Uplink Packet Access (HSUPA) protocol used for mobile network data.</p></td>
</tr>
<tr class="even">
<td>[IPv4LinkMTU](element-ipv4linkmtu.md)</td>
<td><p>Defines the maximum transmission unit (MTU) for an IPv4 link. It must be a positive integer between 1280 and 1500.</p></td>
</tr>
<tr class="odd">
<td>[IPv6LinkMTU](element-ipv6linkmtu.md)</td>
<td><p>Defines the maximum transmission unit (MTU) for an IPv6 link. It must be a positive integer between 1280 and 1500.</p></td>
</tr>
<tr class="even">
<td>[LTE](element-lte.md)</td>
<td><p>Defines the Long Term Evolution (LTE) standard used for mobile network data.</p></td>
</tr>
<tr class="odd">
<td>[MaxNumberOfDevices](element-maxnumberofdevices.md)</td>
<td><p>Defines the maximum number of tethered connections.</p></td>
</tr>
<tr class="even">
<td>[MultiplePDPContextPolicies](element-multiplepdpcontextpolicies.md)</td>
<td><p>Defines multiple Packet Data Protocol (PDP) context policies in a subscriber's carrier provisioning file.</p></td>
</tr>
<tr class="odd">
<td>[NONE](element-none.md)</td>
<td><p>No mobile broadband network Data Class is available.</p></td>
</tr>
<tr class="even">
<td>[Name](element-name.md)</td>
<td><p>Defines the name of a Packet Data Protocol (PDP) context policy in a subscriber's carrier provisioning file.</p></td>
</tr>
<tr class="odd">
<td>[NetworkSettings](element-networksettings.md)</td>
<td><p>Defines the network settings in a subscriber's carrier provisioning file.</p></td>
</tr>
<tr class="even">
<td>[ONEXEVDO](element-onexevdo.md)</td>
<td><p>Defines the Enhanced Voice-Data Optimized (EVDO) standard used for mobile network data.</p></td>
</tr>
<tr class="odd">
<td>[ONEXEVDO_REVA](element-onexevdo-reva.md)</td>
<td><p>Defines the Enhanced Voice-Data Optimized (EVDO) Revision A (Rev. A) standard used for mobile network data.</p></td>
</tr>
<tr class="even">
<td>[ONEXEVDO_REVB](element-onexevdo-revb.md)</td>
<td><p>Defines the Enhanced Voice-Data Optimized (EVDO) Revision B (Rev. B) standard used for mobile network data.</p></td>
</tr>
<tr class="odd">
<td>[ONEXEVDV](element-onexevdv.md)</td>
<td><p>Defines the 1x Evolution-Data and Voice (1xEV-DV) standards used for mobile network data.</p></td>
</tr>
<tr class="even">
<td>[ONEXRTT](element-onexrtt.md)</td>
<td><p>Defines the 1x Radio Transmission Technology (1xRTT) standards used for mobile network data.</p></td>
</tr>
<tr class="odd">
<td>[PDPContextPolicy](element-pdpcontextpolicy.md)</td>
<td><p>Defines a Packet Data Protocol (PDP) context policy in a subscriber's carrier provisioning file.</p></td>
</tr>
<tr class="even">
<td>[Password](element-password.md)</td>
<td><p>Defines the password used for the Packet Data Protocol (PDP) context activation.</p></td>
</tr>
<tr class="odd">
<td>[THREEXRTT](element-threexrtt.md)</td>
<td><p>Defines the 3X Radio Transmission Technology (3xRTT) standard used for mobile network data.</p></td>
</tr>
<tr class="even">
<td>[TetheringProfile](element-tetheringprofile.md)</td>
<td><p>Defines the tethering profile in a subscriber's carrier provisioning file.</p></td>
</tr>
<tr class="odd">
<td>[TetheringSettings](element-tetheringsettings.md)</td>
<td><p>Defines the tethering settings in a subscriber's carrier provisioning file.</p></td>
</tr>
<tr class="even">
<td>[UMB](element-umb.md)</td>
<td><p>Defines the Ultra Mobile Broadband (UMB) system used for mobile network data.</p></td>
</tr>
<tr class="odd">
<td>[UMTS](element-umts.md)</td>
<td><p>Defines the Universal Mobile Telecommunications System (UMTS) protocol used for mobile network data based on the GSM standard.</p></td>
</tr>
<tr class="even">
<td>[UserLogonCred](element-userlogoncred.md)</td>
<td><p>Defines the user login credentials for a context in the Packet Data Protocol (PDP) context policy.</p></td>
</tr>
<tr class="odd">
<td>[UserName](element-username.md)</td>
<td><p>Defines the username used for the Packet Data Protocol (PDP) context activation.</p></td>
</tr>
</tbody>
</table>

 

The full CarrierControlSchema\_v2 schema is below:

``` syntax
<xs:schema targetNamespace="http://www.microsoft.com/networking/CarrierControl/v2"
    elementFormDefault="qualified"
    xmlns="http://www.microsoft.com/networking/CarrierControl/v2"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:base="http://www.microsoft.com/networking/CarrierControl/Base/v1"
>

  <xs:import namespace="http://www.microsoft.com/networking/CarrierControl/Base/v1" />

  <xs:complexType name="ApnContextType">
    <xs:sequence>
      <xs:element name="AccessString" minOccurs="0">
        <xs:simpleType>
          <xs:restriction base="xs:token">
            <xs:minLength value="1"/>
            <xs:maxLength value="100"/>
          </xs:restriction>
        </xs:simpleType>
      </xs:element>
      <xs:element name="UserLogonCred" minOccurs="0">
        <xs:complexType>
          <xs:sequence>
            <xs:element name="UserName" type="base:NameType"/>
            <xs:element name="Password" type="xs:string" minOccurs="0"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="Compression" minOccurs="0">
        <xs:simpleType>
          <xs:restriction base="xs:token">
            <xs:enumeration value="DISABLE"/>
            <xs:enumeration value="ENABLE"/>
          </xs:restriction>
        </xs:simpleType>
      </xs:element>
      <xs:element name="AuthProtocol" minOccurs="0">
        <xs:simpleType>
          <xs:restriction base="xs:token">
            <xs:enumeration value="NONE"/>
            <xs:enumeration value="PAP"/>
            <xs:enumeration value="CHAP"/>
            <xs:enumeration value="MsCHAPv2"/>
          </xs:restriction>
        </xs:simpleType>
      </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="MTUType">
    <xs:restriction base="xs:positiveInteger">
      <xs:minInclusive value="1280" />
      <xs:maxInclusive value="1500" />
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="DNSRetryIntervalType">
    <xs:restriction base="xs:positiveInteger">
      <xs:minInclusive value="1" />
      <xs:maxInclusive value="4" />
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="DNSRetryCountType">
    <xs:restriction base="xs:positiveInteger">
      <xs:minInclusive value="1" />
      <xs:maxInclusive value="4" />
    </xs:restriction>
  </xs:simpleType>
  
  <xs:complexType name="DNSRetrySettingsType">
    <xs:sequence>
      <xs:element name="DNSRetryIntervalInSeconds" type="DNSRetryIntervalType" />
      <xs:element name="DNSRetryCount" type="DNSRetryCountType" />
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="FriendlyNameType">
    <xs:restriction base="xs:normalizedString">
      <xs:minLength value="1" />
      <xs:maxLength value="15" />
      <xs:whiteSpace value="collapse" />
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="TetheringMaxNumberofDeviceType">
    <xs:restriction base="xs:positiveInteger" >
      <xs:minInclusive value="3"/>
      <xs:maxInclusive value="10"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="PhoneNumberType">
    <xs:restriction base="xs:normalizedString">
      <xs:minLength value="0" />
      <xs:maxLength value="25" />
      <xs:whiteSpace value="collapse" />
    </xs:restriction>
  </xs:simpleType>

  <xs:complexType name="NetworkSettingsType">
    <xs:sequence>
      <xs:element name="IPv4LinkMTU" type="MTUType" minOccurs="0" />
      <xs:element name="IPv6LinkMTU" type="MTUType" minOccurs="0" />
      <xs:element name="DNSRetrySettings" type="DNSRetrySettingsType" minOccurs="0" />
    </xs:sequence>

  </xs:complexType>

  <xs:complexType name="DataClassFriendlyNamesType">
    <xs:sequence>
      <xs:element name="NONE" type="FriendlyNameType" minOccurs="0" />
      <xs:element name="GPRS" type="FriendlyNameType" minOccurs="0" />
      <xs:element name="EDGE" type="FriendlyNameType" minOccurs="0" />
      <xs:element name="UMTS" type="FriendlyNameType" minOccurs="0" />
      <xs:element name="HSDPA" type="FriendlyNameType" minOccurs="0" />
      <xs:element name="HSUPA" type="FriendlyNameType" minOccurs="0" />
      <xs:element name="LTE" type="FriendlyNameType" minOccurs="0" />
      <xs:element name="ONEXRTT" type="FriendlyNameType" minOccurs="0" />
      <xs:element name="ONEXEVDO" type="FriendlyNameType" minOccurs="0" />
      <xs:element name="ONEXEVDO_REVA" type="FriendlyNameType" minOccurs="0" />
      <xs:element name="ONEXEVDV" type="FriendlyNameType" minOccurs="0" />
      <xs:element name="THREEXRTT" type="FriendlyNameType" minOccurs="0" />
      <xs:element name="ONEXEVDO_REVB" type="FriendlyNameType" minOccurs="0" />
      <xs:element name="UMB" type="FriendlyNameType" minOccurs="0" />
      <xs:element name="CUSTOM" type="FriendlyNameType" minOccurs="0" />
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="AppIDListType">
    <xs:sequence>
      <xs:element name="AppID" type="xs:string" minOccurs="0"  maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="PDPContextPolicyType">
    <xs:sequence>
      <xs:element name="Name" type="base:NameType" />
      <xs:element name="Context" type="ApnContextType" />
      <xs:element name="AppIDList" type="AppIDListType" />
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="MultiplePDPContextPoliciesType">
    <xs:sequence>
      <xs:element name="PDPContextPolicy" type="PDPContextPolicyType" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
    <xs:attribute name="MultiplePDPContextSupport" type="xs:boolean" default="true" />
  </xs:complexType>
  
  <xs:complexType name="TetheringProfileType">
  <xs:sequence>
    <xs:element name="Name" type="base:NameType" />
    <xs:element name="Context" type="ApnContextType" />
  </xs:sequence>
  </xs:complexType>
  
  <xs:complexType name="TetheringSettingsType">
     <xs:sequence>
      <xs:element name="TetheringProfile" type="TetheringProfileType" minOccurs="0" />
       <xs:element name="MaxNumberOfDevices" type="TetheringMaxNumberofDeviceType" minOccurs="0" />
     </xs:sequence>
  </xs:complexType>
  

  <xs:element name="Extensions_v2">
    <xs:complexType>
      <xs:sequence>

        <xs:element name="CarrierNetworkMetadata" minOccurs="0">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="NetworkSettings"  type="NetworkSettingsType" minOccurs="0" />
              <xs:element name="DataClassFriendlyNames" type="DataClassFriendlyNamesType" minOccurs="0" />
              <xs:element name="CustomerSupportPhoneNumber" type="PhoneNumberType" minOccurs="0" />

            </xs:sequence>
          </xs:complexType>
        </xs:element>

        <xs:element name="AdditionalPDPContexts" minOccurs="0">
          <xs:complexType>
            <xs:sequence>

              <xs:element name="MultiplePDPContextPolicies" type="MultiplePDPContextPoliciesType" minOccurs="0"  />
              <xs:element name="TetheringSettings" type="TetheringSettingsType" minOccurs="0" />

            </xs:sequence>
          </xs:complexType>
        </xs:element>
  
      </xs:sequence>
    </xs:complexType>
  </xs:element>

</xs:schema>
```

## Related topics


[CarrierControlSchema schema](https://msdn.microsoft.com/library/windows/apps/hh868312)

 

 



