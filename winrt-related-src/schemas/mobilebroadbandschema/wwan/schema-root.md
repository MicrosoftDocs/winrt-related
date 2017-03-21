---
title: WWAN Schema
description: The WWAN schema defines elements that are used to describe a subscriber's connection to a Wireless Wide Area Network (WWAN).
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# WWAN Schema


The WWAN schema defines elements that are used to describe a subscriber's connection to a Wireless Wide Area Network (WWAN). All of the elements are in the namespace http://www.microsoft.com/networking/CarrierControl/WWAN/v1. Not all elements are in every profile, as some elements are optional.

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
<td><p>Defines the Access Point Name (APN) or dial string to be used to establish a data connection. Must be less than 100 characters.</p></td>
</tr>
<tr class="even">
<td>[ActivationComplete](element-activationcomplete.md)</td>
<td><p>If <strong>true</strong>, the subscription has been activated, and the machine should immediately attempt to connect. Otherwise, <strong>false</strong>.</p></td>
</tr>
<tr class="odd">
<td>[ActivationMethod](element-activationmethod.md)</td>
<td><p>Defines the abstract base element for [<strong>ReconnectToNetwork</strong>](element-reconnecttonetwork.md), [<strong>ReregisterToNetwork</strong>](element-reregistertonetwork.md), and [<strong>ServiceActivation</strong>](element-serviceactivation.md).</p></td>
</tr>
<tr class="even">
<td>[AssociatedPlan](element-associatedplan.md)</td>
<td><p>Contains the name of the subscriber's data plan. It must match the <strong>Name</strong> attribute of a [<strong>Plan</strong>](https://msdn.microsoft.com/library/windows/apps/hh868373) in the same XML document.</p></td>
</tr>
<tr class="odd">
<td>[AuthProtocol](element-authprotocol.md)</td>
<td><p>Defines the authentication protocol to be used for activating a Packet Data Protocol (PDP) context:</p>
<p></p>
<ul>
<li><strong>NONE</strong> - No authentication protocol.</li>
<li><strong>PAP</strong> - Unencrypted password authentication.</li>
<li><strong>CHAP</strong> - Challenge Handshake Authentication Protocol(CHAP).</li>
<li><strong>MsCHAPv2</strong> - Microsoft’s Challenge Handshake Authentication Protocol(CHAP) v2.0.</li>
</ul></td>
</tr>
<tr class="even">
<td>[Branding](element-branding.md)</td>
<td><p>Defines carrier specific branding information for a subscriber's connection to the Mobile Network Operator (MNO).</p></td>
</tr>
<tr class="odd">
<td>[CarrierSpecificData](element-carrierspecificdata.md)</td>
<td><p>Defines carrier specific data not specified by Windows.</p></td>
</tr>
<tr class="even">
<td>[Compression](element-compression.md)</td>
<td><p>If <strong>ENABLE</strong>, the packet header and data transferred over the connection is compressed. Otherwise, <strong>DISABLE</strong>.</p></td>
</tr>
<tr class="odd">
<td>[Congested](element-congested.md)</td>
<td><p>If <strong>true</strong>, the subscriber's connection is in a state of congestion. Otherwise, it is either not supported by the MNO or <strong>false</strong>.</p></td>
</tr>
<tr class="even">
<td>[Context](element-context.md)</td>
<td><p>Defines the parameters required to setup a data connection.</p></td>
</tr>
<tr class="odd">
<td>[DataLimit](element-datalimit.md)</td>
<td><p>Defines a value representing the data limit in MB for a capped plan. Must be a value from 0 to 2<sup>32nd</sup>.</p></td>
</tr>
<tr class="even">
<td>[DataRoamingPartners](element-dataroamingpartners.md)</td>
<td><p>Defines the list of preferred network providers for roaming.</p></td>
</tr>
<tr class="odd">
<td>[DefaultProfile](element-defaultprofile.md)</td>
<td><p>Defines the default connection profile used by a subscriber to connect to a MNO. The Mobile Broadband service will use these connection settings without prompting the user for details.</p></td>
</tr>
<tr class="even">
<td>[Description](element-description.md)</td>
<td><p>Defines a brief description of the profile.</p></td>
</tr>
<tr class="odd">
<td>[Extensions](element-extensions.md)</td>
<td><p>Defines a schema extension point container for future additions.</p></td>
</tr>
<tr class="even">
<td>[Fields](element-fields.md)</td>
<td><p>Defines values that describe the subscriber's plan and data usage.</p></td>
</tr>
<tr class="odd">
<td>[HomeProviderName](element-homeprovidername.md)</td>
<td><p>Defines the name of the Home Provider for a given SIM/Device.</p></td>
</tr>
<tr class="even">
<td>[InboundBandwidth](element-inboundbandwidth.md)</td>
<td><p>Defines a value representing the effective link speed of the subscriber’s inbound connection.</p></td>
</tr>
<tr class="odd">
<td>[Locale](element-locale.md)</td>
<td><p>Defines the message country code in the form &quot;en-us&quot; using ISO-3166.</p></td>
</tr>
<tr class="even">
<td>[Logo](element-logo.md)</td>
<td><p>Defines a 32x32 bitmap (.bmp) or portable network graphics (.png) type image of the MNO's logo.</p></td>
</tr>
<tr class="odd">
<td>[Message](element-message.md)</td>
<td><p>Defines a MNO formatted message that contains the parsing rules necessary for Windows 8 to parse the message.</p></td>
</tr>
<tr class="even">
<td>[Messages](element-messages.md)</td>
<td><p>Contains a set of MNO messages that are parsed by Windows 8 and may be signaled to the user.</p></td>
</tr>
<tr class="odd">
<td>[Name (in type: Branding)](element-name.md)</td>
<td><p>Defines a carrier specific branding name for the MNO. Maximum length is 20 characters.</p></td>
</tr>
<tr class="even">
<td>[Name (type: NameType)](element-1-name.md)</td>
<td><p>Defines the profile name. Must be 64 characters or less.</p></td>
</tr>
<tr class="odd">
<td>[OutboundBandwidth](element-outboundbandwidth.md)</td>
<td><p>Defines a value representing the effective link speed of the subscriber’s outbound connection.</p></td>
</tr>
<tr class="even">
<td>[OverDataLimit](element-overdatalimit.md)</td>
<td><p>Defines whether a subscriber has consumed more bytes than the data limit for their plan.</p></td>
</tr>
<tr class="odd">
<td>[Password](element-password.md)</td>
<td><p>Defines the password used to authenticate a user. Must be less than 256 characters.</p></td>
</tr>
<tr class="even">
<td>[Pattern](element-pattern.md)</td>
<td><p>Defines a regular expression describing the contents of the decoded human-readable message.</p></td>
</tr>
<tr class="odd">
<td>[PlanType](element-plantype.md)</td>
<td><p>Defines the type of plan currently in use by the subscriber.</p></td>
</tr>
<tr class="even">
<td>[Provider](element-provider.md)</td>
<td><p>Defines the name and provider ID of a cellular network.</p></td>
</tr>
<tr class="odd">
<td>[PurchaseProfile](element-purchaseprofile.md)</td>
<td><p>Defines a purchase connection profile used by a subscriber to connect to a MNO.</p></td>
</tr>
<tr class="even">
<td>[ReconnectToNetwork](element-reconnecttonetwork.md)</td>
<td><p>Defines timing information used to activate the subscriber's account on the Mobile Broadband Network (MNO) for a reconnect activation type.</p></td>
</tr>
<tr class="odd">
<td>[RefreshProvisioning](element-refreshprovisioning.md)</td>
<td><p>If <strong>true</strong>, the network configuration has been updated, and the machine should attempt to retrieve a new provisioning file during the next available maintenance window. Otherwise, <strong>false</strong>.</p></td>
</tr>
<tr class="even">
<td>[ReregisterToNetwork](element-reregistertonetwork.md)</td>
<td><p>Defines timing information used to activate the subscriber's account on the Mobile Broadband Network (MNO) for a reregister activation type.</p></td>
</tr>
<tr class="odd">
<td>[SMSBearer](element-smsbearer.md)</td>
<td><p>Defines bearer types allowed for SMS messages.</p></td>
</tr>
<tr class="even">
<td>[ServiceActivation](element-serviceactivation.md)</td>
<td><p>Defines carrier specific information required to activate the subscriber's account on the Mobile Broadband Network (MNO).</p></td>
</tr>
<tr class="odd">
<td>[USSDBearer](element-ussdbearer.md)</td>
<td><p>Defines bearer types allowed for USSD messages.</p></td>
</tr>
<tr class="even">
<td>[Units](element-units.md)</td>
<td><p>Defines how to interpret the unit fields corresponding to each number field. Carriers may specify a whitespace-delimited list of tokens corresponding to each of the supported multipliers.</p></td>
</tr>
<tr class="odd">
<td>[Usage](element-usage.md)</td>
<td><p>Defines the number of bytes the subscriber has consumed against their data limit. If absent, it is inferred by:</p>
<ul>
<li><strong>UsagePercentage</strong> times <strong>DataLimit</strong></li>
<li><strong>UsagePercentage</strong> times <strong>DataLimit</strong></li>
<li><strong>UsageOverage</strong> plus <strong>DataLimit</strong></li>
<li>(<strong>UsageOveragePercentage</strong> times <strong>DataLimit</strong>) plus <strong>DataLimit</strong></li>
<li><strong>UsageOverage</strong> plus (<strong>UsageOverage</strong> divided by (<strong>UsageOveragePercentage</strong> - 100) )</li>
<li><strong>UsageOverage</strong> plus <strong>DataLimit</strong></li>
</ul></td>
</tr>
<tr class="even">
<td>[UsageOverage](element-usageoverage.md)</td>
<td><p>Defines the number of bytes the subscriber has consumed over their data limit.</p></td>
</tr>
<tr class="odd">
<td>[UsageOveragePercentage](element-usageoveragepercentage.md)</td>
<td><p>Defines the percentage over the data limit a subscriber has consumed.</p></td>
</tr>
<tr class="even">
<td>[UsagePercentage](element-usagepercentage.md)</td>
<td><p>Defines the percentage of the data limit a subscriber has consumed.</p></td>
</tr>
<tr class="odd">
<td>[UsageTimestamp](element-usagetimestamp.md)</td>
<td><p>Defines a validity date and time of the usage information.</p></td>
</tr>
<tr class="even">
<td>[UserLogonCred](element-userlogoncred.md)</td>
<td><p>Defines logon credentials for a connection.</p></td>
</tr>
<tr class="odd">
<td>[UserName](element-username.md)</td>
<td><p>Defines the user name for logon. Must be less than 256 characters.</p></td>
</tr>
</tbody>
</table>

 

The full WWAN schema is below:

``` syntax
<?xml version="1.0" encoding="utf-8"?>  
<xs:schema targetNamespace="http://www.microsoft.com/networking/CarrierControl/WWAN/v1"  
    elementFormDefault="qualified"  
    xmlns="http://www.microsoft.com/networking/CarrierControl/WWAN/v1"  
    xmlns:xs="http://www.w3.org/2001/XMLSchema"  
    xmlns:base="http://www.microsoft.com/networking/CarrierControl/Base/v1"  
    xmlns:plans="http://www.microsoft.com/networking/CarrierControl/Plans/v1">  
  <xs:import namespace="http://www.microsoft.com/networking/CarrierControl/Base/v1"/>  
  <xs:import namespace="http://www.microsoft.com/networking/CarrierControl/Plans/v1"/>  
  
  <xs:simpleType name="SimIccIDType">  
    <xs:restriction base="xs:token">  
      <xs:pattern value="[a-zA-Z\d]{1,20}"/>  
    </xs:restriction>  
  </xs:simpleType>  
  
  <xs:complexType name="ContextType">  
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
     
  <xs:complexType name="ActivationMethodType">  
    <xs:attribute name="Delay" default="PT0S">  
      <xs:simpleType>  
        <xs:restriction base="xs:duration">  
          <xs:minInclusive value="PT0S"/>  
          <xs:maxExclusive value="PT1H"/>  
        </xs:restriction>  
      </xs:simpleType>  
    </xs:attribute>  
    <xs:attribute name="RetryCount" default="0">  
      <xs:simpleType>  
        <xs:restriction base="xs:nonNegativeInteger">  
          <xs:maxInclusive value="10"/>  
        </xs:restriction>  
      </xs:simpleType>  
    </xs:attribute>  
    <xs:attribute name="RetryInterval" default="PT1M">  
      <xs:simpleType>  
        <xs:restriction base="xs:duration">  
          <xs:minInclusive value="PT1M"/>  
          <xs:maxInclusive value="PT1H"/>  
        </xs:restriction>  
      </xs:simpleType>  
    </xs:attribute>  
  </xs:complexType>  
  <xs:element name="ActivationMethod" type="ActivationMethodType" abstract="true"/>  
  <xs:element name="ReregisterToNetwork" type="ActivationMethodType" substitutionGroup="ActivationMethod"/>  
  <xs:element name="ReconnectToNetwork" type="ActivationMethodType" substitutionGroup="ActivationMethod"/>  
  <xs:element name="ServiceActivation" substitutionGroup="ActivationMethod">  
    <xs:complexType>  
      <xs:complexContent>  
        <xs:extension base="ActivationMethodType">  
          <xs:sequence>  
            <xs:element name="CarrierSpecificData" type="xs:base64Binary"/>  
          </xs:sequence>  
        </xs:extension>  
      </xs:complexContent>  
    </xs:complexType>  
  </xs:element>  
  
  <xs:complexType name="CarrierMBNProfile">  
    <xs:sequence>  
      <xs:element name="Name" type="base:NameType"/>  
      <!-- Brief description of the profile -->  
      <xs:element name="Description" type="base:NameType" minOccurs="0"/>  
  
      <xs:element name="AssociatedPlan" type="xs:string" minOccurs="0"/>  
  
      <xs:element name="HomeProviderName" type="base:ProviderNameType" minOccurs="0"/>  
   
      <xs:element name="Context" type="ContextType" minOccurs="0"/>  
  
      <xs:element name="DataRoamingPartners" minOccurs="0">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element name="Provider" type="base:ProviderType" maxOccurs="unbounded"/>  
          </xs:sequence>  
        </xs:complexType>  
      </xs:element>  
  
      <xs:element name="Extensions" minOccurs="0">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />  
          </xs:sequence>  
        </xs:complexType>  
      </xs:element>  
    </xs:sequence>  
    <xs:attribute name="Priority" type="base:Priority" default="5"/>  
  </xs:complexType>  
  
  <xs:element name="DefaultProfile" type="CarrierMBNProfile"/>  
  <xs:element name="PurchaseProfile" type="CarrierMBNProfile"/>  

  <xs:element name="Branding" type="Branding" />   
  <xs:complexType name="Branding">  
    <xs:sequence>
      <xs:element name="Logo" type="xs:base64Binary" minOccurs="0"/>  
      <xs:element name="Name" minOccurs="0">  
        <xs:simpleType>  
          <xs:restriction base="xs:string">  
            <xs:maxLength value="20"/>  
          </xs:restriction>  
        </xs:simpleType>  
      </xs:element>  
        
      <xs:any namespace="##other" minOccurs="0" maxOccurs="unbounded"/>  
    </xs:sequence>  
  </xs:complexType>  

  <xs:complexType name="BooleanField">  
    <xs:attribute name="TrueToken" type="xs:token"/>  
    <xs:attribute name="FalseToken" type="xs:token"/>  
    <xs:attribute name="Default" type="xs:boolean" default="false"/>  
    <xs:attribute name="Group" type="xs:positiveInteger"/>  
  </xs:complexType>  
  
  <xs:complexType name="DateTimeField">  
    <xs:attribute name="Format" type="xs:string" use="required"/>  
    <xs:attribute name="Group" type="xs:positiveInteger" use="required"/>  
  </xs:complexType>  
  
  <xs:complexType name="NumberField">  
    <xs:attribute name="Group" type="xs:positiveInteger" use="required"/>  
    <xs:attribute name="UnitGroup" type="xs:positiveInteger"/>  
    <xs:attribute name="DefaultUnit" default="None">  
      <xs:simpleType>  
        <xs:restriction base="xs:token">  
          <xs:enumeration value="None"/>  
          <xs:enumeration value="K"/>  
          <xs:enumeration value="M"/>  
          <xs:enumeration value="G"/>  
          <xs:enumeration value="T"/>  
          <xs:enumeration value="Ki"/>  
          <xs:enumeration value="Mi"/>  
          <xs:enumeration value="Gi"/>  
          <xs:enumeration value="Ti"/>  
        </xs:restriction>  
      </xs:simpleType>  
    </xs:attribute>  
  </xs:complexType>  
  
  <xs:complexType name="PercentField">  
    <xs:attribute name="Group" type="xs:positiveInteger" use="required"/>  
  </xs:complexType>  
  
  <xs:simpleType name="TokenList">  
    <xs:list itemType="xs:token"/>  
  </xs:simpleType>

  <xs:element name="SMSBearer">  
    <xs:complexType>  
      <xs:attribute name="Sender" type="xs:token"/>  
      <xs:attribute name="ClassZeroOnly" type="xs:boolean" default="true"/>  
    </xs:complexType>  
  </xs:element>  
  <xs:element name="USSDBearer"/>  
   
  <xs:element name="Messages">  
    <xs:complexType>  
      <xs:sequence>  
        <xs:element name="Message" maxOccurs="unbounded">  
          <xs:complexType>  
            <xs:sequence>  
              <xs:choice>  
                <xs:sequence>  
                  <xs:element ref="SMSBearer" maxOccurs="unbounded"/>  
                  <xs:element ref="USSDBearer" minOccurs="0"/>  
                </xs:sequence>  
                <xs:sequence>  
                  <xs:element ref="USSDBearer"/>  
                </xs:sequence>  
              </xs:choice>  
              <xs:element name="Pattern" type="xs:string"/>  
              <xs:element name="Locale" default="English_United States.1252" minOccurs="0">  
                <xs:simpleType>  
                  <xs:restriction base="xs:token">  
                    <xs:pattern value="\w+(?:_[\w ]+)?(?:\.\d+)?"/>  
                  </xs:restriction>  
                </xs:simpleType>  
              </xs:element>  

              <xs:element name="Units" minOccurs="0">  
                <xs:complexType>  
                    
                  <!-- Powers of 1,000 -->  
                  <xs:attribute name="K" type="TokenList"/>  
                  <xs:attribute name="M" type="TokenList"/>  
                  <xs:attribute name="G" type="TokenList"/>  
                  <xs:attribute name="T" type="TokenList"/>  
  
                  <!-- Powers of 1,024 -->  
                  <xs:attribute name="Ki" type="TokenList"/>  
                  <xs:attribute name="Mi" type="TokenList"/>  
                  <xs:attribute name="Gi" type="TokenList"/>  
                  <xs:attribute name="Ti" type="TokenList"/>  
                    
                </xs:complexType>  
              </xs:element>  
              <xs:element name="Fields" minOccurs="0">  
                <xs:complexType>  
                  <xs:all>   
                    <xs:element name="Usage" type="NumberField" minOccurs="0"/>  
                    <xs:element name="UsagePercentage" type="PercentField" minOccurs="0"/>  
                    <xs:element name="UsageTimestamp" type="DateTimeField" minOccurs="0"/>  
                    <xs:element name="UsageOverage" type="NumberField" minOccurs="0"/>  
                    <xs:element name="UsageOveragePercentage" type="PercentField" minOccurs="0"/>  
                    <xs:element name="DataLimit" type="NumberField" minOccurs="0"/>  
                    <xs:element name="OverDataLimit" type="BooleanField" minOccurs="0"/>
                    <xs:element name="Congested" type="BooleanField" minOccurs="0"/>  
                    <xs:element name="InboundBandwidth" type="NumberField" minOccurs="0"/>  
                    <xs:element name="OutboundBandwidth" type="NumberField" minOccurs="0"/>  
                    <xs:element name="PlanType" minOccurs="0">  
                      <xs:complexType>  
                        <xs:attribute name="Group" type="xs:positiveInteger"/>  
                        <xs:attribute name="Default" type="plans:PlanType"/>  
                        <xs:attribute name="UnrestrictedTokens" type="TokenList"/>  
                        <xs:attribute name="FixedTokens" type="TokenList"/>  
                        <xs:attribute name="VariableTokens" type="TokenList"/>  
                      </xs:complexType>  
                    </xs:element>  
                    <xs:element name="RefreshProvisioning" type="BooleanField" minOccurs="0"/>  
                    <xs:element name="ActivationComplete" type="BooleanField" minOccurs="0"/>  
                  </xs:all>  
                </xs:complexType>  
              </xs:element>  
            </xs:sequence>  
            <xs:attribute name="Silent" type="xs:boolean" default="true"/>  
          </xs:complexType>  
        </xs:element>  
      </xs:sequence>  
    </xs:complexType>  
  </xs:element>  
</xs:schema>
```

 

 



