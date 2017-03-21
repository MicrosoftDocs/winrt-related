---
Description: The HotspotProfile schema defines elements that are used to describe login credentials for Wi-Fi hotspots that use the Wireless Internet Service Provider roaming (WISPr) protocol.
Search.Product: eADQiWindows 10XVcnh
title: HotspotProfile schema
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# HotspotProfile schema


The HotspotProfile schema defines elements that are used to describe login credentials for Wi-Fi hotspots that use the Wireless Internet Service Provider roaming (WISPr) protocol. All of the elements are in the namespace http://www.microsoft.com/networking/WLAN/HotspotProfile/v1. Not all elements are in every profile, as some elements are optional.

The full HotspotProfile schema is below:

``` syntax
﻿<?xml version="1.0" encoding="UTF-8"?>  
<xs:schema targetNamespace="http://www.microsoft.com/networking/WLAN/HotspotProfile/v1"  
    elementFormDefault="qualified"  
    xmlns="http://www.microsoft.com/networking/WLAN/HotspotProfile/v1"  
    xmlns:xs="http://www.w3.org/2001/XMLSchema">  
  
  <xs:element name="BasicAuth">  
    <xs:complexType>  
      <xs:sequence>  
        <xs:element name="UserName" type="xs:token"/>  
        <xs:element name="Password" type="xs:token"/>  
      </xs:sequence>  
    </xs:complexType>  
  </xs:element>  
  
  <xs:element name="ExtAuth">  
    <xs:complexType>  
      <xs:sequence>  
        <xs:element name="ExtensionId" type="xs:token"/>  
      </xs:sequence>  
    </xs:complexType>  
  </xs:element>  
  
  <xs:element name="TrustedDomains">  
    <xs:annotation>  
      <xs:documentation xml:lang="en">  
        The element contains a set of host names that are trusted for providing credentials over HTTPS.  
        A domain name is either a fully qualified name such as hotspot.contoso.com  
        or a wildcard such as .contoso.com to refer to all hosts under the given domain name.  
      </xs:documentation>  
    </xs:annotation>  
    <xs:complexType>  
      <xs:sequence>  
        <xs:element name="TrustedDomain" maxOccurs="unbounded" type="xs:token"/>  
      </xs:sequence>  
    </xs:complexType>  
  </xs:element>  
  
  <xs:element name="SSIDConfig">  
    <xs:annotation>  
      <xs:documentation xml:lang="en">  
        The element contains a set of additional SSID's that are handled by this profile  
        to reduce the number of SSID's in the WLAN profile store.  
        Windows will not auto-connect to these SSID's until a user manually connects  
        and sets the auto-connect flag for a specific SSID.  
      </xs:documentation>  
    </xs:annotation>  
    <xs:complexType>  
      <xs:sequence>  
        <xs:element name="SSID" maxOccurs="250">  
          <xs:complexType>  
            <xs:choice>  
              <xs:element name="hex">  
                <xs:simpleType>  
                  <xs:restriction base="xs:hexBinary">  
                    <xs:minLength value="1" />  
                    <xs:maxLength value="32" />  
                  </xs:restriction>  
                </xs:simpleType>  
              </xs:element>  
              <xs:element name="hexPrefix">  
                <xs:simpleType>  
                  <xs:restriction base="xs:hexBinary">  
                    <xs:minLength value="4" />  
                    <xs:maxLength value="32" />  
                  </xs:restriction>  
                </xs:simpleType>  
              </xs:element>  
              <xs:element name="name">  
                <xs:simpleType>  
                  <xs:restriction base="xs:string">  
                    <xs:minLength value="1" />  
                    <xs:maxLength value="32" />  
                  </xs:restriction>  
                </xs:simpleType>  
              </xs:element>  
              <xs:element name="namePrefix">  
                <xs:simpleType>  
                  <xs:restriction base="xs:string">  
                    <xs:minLength value="4" />  
                    <xs:maxLength value="32" />  
                  </xs:restriction>  
                </xs:simpleType>  
              </xs:element>  
            </xs:choice>  
          </xs:complexType>  
        </xs:element>  
      </xs:sequence>  
    </xs:complexType>  
  </xs:element>  
  
  <xs:element name="HotspotProfile">  
    <xs:complexType>  
      <xs:sequence>  
        <xs:choice>  
          <xs:sequence>  
            <xs:element ref="BasicAuth"/>  
            <xs:element ref="TrustedDomains"/>  
          </xs:sequence>  
          <xs:sequence>  
            <xs:element ref="ExtAuth"/>  
            <xs:element ref="TrustedDomains" minOccurs="0"/>  
          </xs:sequence>  
        </xs:choice>  
        <xs:element name="UserAgent" minOccurs="0" type="xs:token"/>  
        <xs:element ref="SSIDConfig" minOccurs="0"/>  
  
        <!-- extension point -->  
        <xs:any processContents="lax" namespace="##other" minOccurs="0" maxOccurs="unbounded"/>  
      </xs:sequence>  
    </xs:complexType>  
  </xs:element>  
</xs:schema>
```

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
<td>[BasicAuth](element-basicauth.md)</td>
<td><p>Contains the user name and password required for WISPr authentication. Using [<strong>BasicAuth</strong>](element-basicauth.md) allows a static set of credentials to be used; use [<strong>ExtAuth</strong>](element-extauth.md) to have an app generate credentials for WISPr authentication.</p></td>
</tr>
<tr class="even">
<td>[ExtAuth](element-extauth.md)</td>
<td><p>Contains the parameters for handling WISPr authentication through an app (rather than specifying a static user name and password via [<strong>BasicAuth</strong>](element-basicauth.md)).</p></td>
</tr>
<tr class="odd">
<td>[ExtensionId](element-extensionid.md)</td>
<td><p>The package family name of the app that will be invoked to handle the WISPr authentication.</p></td>
</tr>
<tr class="even">
<td>[HotspotProfile](element-hotspotprofile.md)</td>
<td><p>Defines the properties and login credentials for a Wi-Fi hotspot. [<strong>HotspotProfile</strong>](element-hotspotprofile.md) is the unique root element of a Wi-Fi hotspot profile that uses the Wireless Internet Service Provider roaming (WISPr) protocol.</p></td>
</tr>
<tr class="odd">
<td>[Password](element-password.md)</td>
<td><p>Password to be used for WISPr authentication.</p></td>
</tr>
<tr class="even">
<td>[SSID](element-ssid.md)</td>
<td><p>An additional SSID handled by this profile.</p></td>
</tr>
<tr class="odd">
<td>[SSIDConfig](element-ssidconfig.md)</td>
<td><p>Contains a set of additional SSIDs that are handled by this profile to reduce the number of SSIDs in the WLAN profile store. Windows will not connect to these SSIDs until a user manually connects once. The newly-created profile will inherit the HotspotAuth settings from this profile.</p></td>
</tr>
<tr class="even">
<td>[TrustedDomain](element-trusteddomain.md)</td>
<td><p>A host name that is trusted for providing credentials over HTTPS. Can be either a fully qualified name (such as <em>hotspot.contoso.com</em>) or a wildcard to refer to all hosts under the given domain name (such as <em>.contoso.com</em>).</p></td>
</tr>
<tr class="odd">
<td>[TrustedDomains](element-trusteddomains.md)</td>
<td><p>Contains a set of one or more host names that are trusted for providing credentials over HTTPS. Can be either a fully qualified name (such as <em>hotspot.contoso.com</em>) or a wildcard to refer to all hosts under the given domain name (such as <em>.contoso.com</em>).</p></td>
</tr>
<tr class="even">
<td>[UserAgent](element-useragent.md)</td>
<td><p>Customized HTTP user agent string to support operator-specific user agent filtering. This element is optional.</p></td>
</tr>
<tr class="odd">
<td>[UserName](element-username.md)</td>
<td><p>User name to be used for WISPr authentication.</p></td>
</tr>
<tr class="even">
<td>[hex](element-hex.md)</td>
<td><p>Defines the SSID of a wireless LAN in hexadecimal format.</p></td>
</tr>
<tr class="odd">
<td>[hexPrefix](element-hexprefix.md)</td>
<td><p>Defines a class of wireless LANs whose SSIDs begin with the bytes provided.</p></td>
</tr>
<tr class="even">
<td>[name](element-name.md)</td>
<td><p>Defines the SSID of a wireless LAN in alphanumeric format.</p></td>
</tr>
<tr class="odd">
<td>[namePrefix](element-nameprefix.md)</td>
<td><p>Defines a class of wireless LANs whose SSIDs begin with the characters provided.</p></td>
</tr>
</tbody>
</table>

 

 

 



