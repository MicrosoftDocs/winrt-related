---
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# WLAN schema


The WLAN schema defines elements that are used to describe a subscriber's connection to a Wireless Local Area Network (WLAN).

All of the elements in the WLAN schema are in the *http://www.microsoft.com/networking/CarrierControl/WLAN/v1* namespace.

The [WLAN\_v2](https://msdn.microsoft.com/library/windows/apps/dn297323) schema defines additional elements in the *http://www.microsoft.com/networking/CarrierControl/WLAN/v2* namespace and is supported on Windows 8.1, Windows Server 2012 R2, and later.

The [**SSIDConfig**](element-ssidconfig.md) element in the WLAN schema supports up to 25 SSIDs in the v1 namespace and up to additional 10,000 SSIDs in the v2 namespace. The v2 namespace also supports [**SSIDPrefix**](https://msdn.microsoft.com/library/windows/apps/dn297316) elements.

Not all elements are in every profile, as some elements are optional.

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
<td>[AssociatedPlan](element-associatedplan.md)</td>
<td><p>Contains the name of the subscriber's data plan. It must match the <strong>Name</strong> attribute of a [<strong>Plan</strong>](https://msdn.microsoft.com/library/windows/apps/hh868373) in the same XML document.</p></td>
</tr>
<tr class="even">
<td>[MSM](element-msm.md)</td>
<td><p>Defines various media-specific module (MSM) settings for this profile on a WLAN.</p></td>
</tr>
<tr class="odd">
<td>[PMKCacheMode](element-pmkcachemode.md)</td>
<td><p>Defines whether Pairwise Master Key (PMK) caching is to be used by this profile to connect to a WLAN.</p></td>
</tr>
<tr class="even">
<td>[PMKCacheSize](element-pmkcachesize.md)</td>
<td><p>Defines the number of entries in the Pairwise Master Key (PMK) cache on the client. Must be a value between 1 and 255 inclusive.</p></td>
</tr>
<tr class="odd">
<td>[PMKCacheTTL](element-pmkcachettl.md)</td>
<td><p>Defines the length of time, in minutes, that a Pairwise Master Key (PMK) cache will be kept. Must be a value between 5 and 1440 inclusive.</p></td>
</tr>
<tr class="even">
<td>[SSID](element-ssid.md)</td>
<td><p>Contains the SSID for a WLAN.</p></td>
</tr>
<tr class="odd">
<td>[SSIDConfig](element-ssidconfig.md)</td>
<td><p>Defines one or more service set identifiers (SSID) for a wireless LAN.</p></td>
</tr>
<tr class="even">
<td>[WLANProfile](element-wlanprofile.md)</td>
<td><p>Defines the properties and security settings of a subscriber's WLAN connection profile. [<strong>WLANProfile</strong>](element-wlanprofile.md) is the unique root element of a wireless profile.</p></td>
</tr>
<tr class="odd">
<td>[authEncryption](element-authencryption.md)</td>
<td><p>Defines the authentication and encryption pair to be used for this profile on a WLAN.</p></td>
</tr>
<tr class="even">
<td>[authentication](element-authentication.md)</td>
<td><p>Defines the authentication method to be used by this profile to connect to a WLAN.</p></td>
</tr>
<tr class="odd">
<td>[encryption](element-encryption.md)</td>
<td><p>Defines the type of data encryption to be used by this profile to connect to a WLAN.</p></td>
</tr>
<tr class="even">
<td>[hex](element-hex.md)</td>
<td><p>Defines the SSID of a wireless LAN in hexadecimal format.</p></td>
</tr>
<tr class="odd">
<td>[keyIndex](element-keyindex.md)</td>
<td><p>Defines which key index should be used to encrypt wireless traffic. [<strong>keyIndex</strong>](element-keyindex.md) is only used when [<strong>keyType</strong>](element-keytype.md) is <strong>networkKey</strong>. The default value is 0 when [<strong>sharedKey</strong>](element-sharedkey.md) is present. Must be a value between 0 and 3 inclusive.</p></td>
</tr>
<tr class="even">
<td>[keyMaterial](element-keymaterial.md)</td>
<td><p>Defines a network key or pass phrase. If [<strong>protected</strong>](element-protected.md) is <strong>true</strong>, then the key material is encrypted; otherwise, the key material is unencrypted. Encrypted key material is expressed in hexadecimal form.</p></td>
</tr>
<tr class="odd">
<td>[keyType](element-keytype.md)</td>
<td><p>Defines whether the shared key will be a network key or a pass phrase.</p></td>
</tr>
<tr class="even">
<td>[name (in SSID)](element-1-name.md)</td>
<td><p>Defines the SSID of a wireless LAN in alphanumeric format.</p></td>
</tr>
<tr class="odd">
<td>[name (type: NameType)](element-name.md)</td>
<td><p>Defines the case sensitive name of a wireless LAN profile.</p></td>
</tr>
<tr class="even">
<td>[preAuthMode](element-preauthmode.md)</td>
<td><p>Defines whether pre-authentication will be used by the client.</p></td>
</tr>
<tr class="odd">
<td>[preAuthThrottle](element-preauththrottle.md)</td>
<td><p>Defines the number of pre-authentication attempts to try on neighboring access points (AP). Must be a value between 1 and 16 inclusive.</p></td>
</tr>
<tr class="even">
<td>[protected](element-protected.md)</td>
<td><p>If <strong>true</strong>, the shared key is encrypted. Otherwise, <strong>false</strong>.</p></td>
</tr>
<tr class="odd">
<td>[security](element-security.md)</td>
<td><p>Defines various security settings for this profile on a WLAN.</p></td>
</tr>
<tr class="even">
<td>[sharedKey](element-sharedkey.md)</td>
<td><p>Defines optional shared key information to be used by this profile to connect to a WLAN.</p></td>
</tr>
<tr class="odd">
<td>[useOneX](element-useonex.md)</td>
<td><p>If <strong>true</strong>, 802.1X authentication is to be used by this profile to connect to the WLAN. Otherwise, <strong>false</strong>.</p></td>
</tr>
</tbody>
</table>

 

The full WLAN schema is below:

``` syntax
<?xml version="1.0" encoding="utf-8"?>  
<xs:schema targetNamespace="http://www.microsoft.com/networking/CarrierControl/WLAN/v1"  
    elementFormDefault="qualified"  
    xmlns="http://www.microsoft.com/networking/CarrierControl/WLAN/v1"  
    xmlns:xs="http://www.w3.org/2001/XMLSchema"  
    xmlns:base="http://www.microsoft.com/networking/CarrierControl/Base/v1">  
  <xs:import namespace="http://www.microsoft.com/networking/CarrierControl/Base/v1" />  
  
    <!-- WISPR Credentials in separate schema; uses xs:any tag below -->
  
    <xs:element name="WLANProfile" type="CarrierWLANProfile"/>

  <xs:complexType name="CarrierWLANProfile">  
    <xs:sequence>  
                    
      <!-- Profile name is required. -->        
      <xs:element name="name" type="base:NameType" />
  
      <xs:element name="Associated Plan" type="xs:string" minOccurs="0"/>

      <!-- SSIDs are required. -->        

      <xs:element name="SSIDConfig" maxOccurs="1">  
        <xs:complexType>  
          <xs:sequence>

      <xs:annotation>
         <xs:documentation>
            This element supports up to 25 SSIDs in the v1 namespace and up to additional 10000 SSIDs in the v2 namespace.
            The v2 namespace also supports SSID prefixes.
         </xs:documentation>
      </xs:annotation>

            <xs:element name="SSID" maxOccurs="25">  
              <xs:complexType>  

      <!-- Either Hex or named SSID must be present. -->
          
                <xs:choice>   
                  <xs:element name="hex">  
                    <xs:simpleType>  
                      <xs:restriction base="xs:hexBinary">  
                        <xs:minLength value="1" />  
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
                </xs:choice>  
              </xs:complexType>  
            </xs:element>  

      <!-- SSID and SSIDPrefix elements from v2 namespace can be set here.
        <xs:element name="SSID" minOccurance="0" maxOccurance="10000"
          namespace="http://www.microsoft.com/networking/WLAN/profile/v2"/> 
        <xs:element name="SSIDPrefix" minOccurance="0" maxOccurance="32"
          namespace="http://www.microsoft.com/networking/WLAN/profile/v2"/>
      -->      

      <!-- extension point for other namespaces -->
   
            <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />  
          </xs:sequence>  
        </xs:complexType>  
      </xs:element>  
  
      <!-- wireless LAN MSM settings -->

            <xs:element name="MSM" minOccurs="0">  
              <xs:complexType>  
                <xs:sequence>   

            <!-- security settings -->
                  <xs:element name="security" minOccurs="0">  
                    <xs:complexType>  
                      <xs:sequence>  
                        <xs:element name="authEncryption">  
                          <xs:complexType>  
                            <xs:sequence>
            <!-- valid authentication methods -->   
                              <xs:element name="authentication">  
                                <xs:simpleType>  
                                  <xs:restriction base="xs:string">  
                                    <xs:enumeration value="open" />  
                                    <xs:enumeration value="shared" />  
                                    <xs:enumeration value="WPA" />  
                                    <xs:enumeration value="WPAPSK" />  
                                    <xs:enumeration value="WPA2" />  
                                    <xs:enumeration value="WPA2PSK" />  
                                  </xs:restriction>  
                                </xs:simpleType>  
                              </xs:element>  
            
            <!-- valid encryption methods -->

                              <xs:element name="encryption">  
                                <xs:simpleType>  
                                  <xs:restriction base="xs:string">  
                                    <xs:enumeration value="none" />  
                                    <xs:enumeration value="WEP" />  
                                    <xs:enumeration value="TKIP" />  
                                    <xs:enumeration value="AES" />  
                                  </xs:restriction>  
                                </xs:simpleType>  
                              </xs:element>  

            <!-- flag indicating use of 802.1X -->

                              <xs:element name="useOneX" type="xs:boolean" minOccurs="0" />  

            <!-- extension point for other namespaces; allowed for OneX, etc. -->

                              <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />  
                            </xs:sequence>  
                          </xs:complexType>  
                        </xs:element>

            <!-- Optional MSM security settings. -->
            <!-- there is no default value for sharedKey if absent -->

                        <xs:element name="sharedKey" minOccurs="0">  
                          <xs:complexType>  
                            <xs:sequence>  
                              <xs:element name="keyType">  
                                <xs:simpleType>  
                                  <xs:restriction base="xs:string">  
                                    <xs:enumeration value="networkKey" />  
                                    <xs:enumeration value="passPhrase" />  
                                  </xs:restriction>  
                                </xs:simpleType>  
                              </xs:element>  
                              <xs:element name="protected" type="xs:boolean" />  
                              <xs:element name="keyMaterial" type="xs:string" />  
  
            <!-- extension point for other namespaces -->

                              <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />  
                            </xs:sequence>  
                          </xs:complexType>  
                        </xs:element>

            <!-- the default value is 0 when the shared key is present -->  
  
                        <xs:element name="keyIndex" minOccurs="0">  
                          <xs:simpleType>  
                            <xs:restriction base="xs:integer">  
                              <xs:minInclusive value="0" />  
                              <xs:maxInclusive value="3" />  
                            </xs:restriction>  
                          </xs:simpleType>  
                        </xs:element>  
 
            <!-- For WPA2, the default value is "enabled"
                 for all others, the default value is "disabled"
             -->

                        <xs:element name="PMKCacheMode" minOccurs="0">  
                          <xs:simpleType>  
                            <xs:restriction base="xs:string">  
                              <xs:enumeration value="disabled" />  
                              <xs:enumeration value="enabled" />  
                            </xs:restriction>  
                          </xs:simpleType>  
                        </xs:element>  
   
           <!-- the default value is 720 minutes -->

                        <xs:element name="PMKCacheTTL" minOccurs="0">  
                          <xs:simpleType>  
                            <xs:restriction base="xs:integer">  
                              <xs:minInclusive value="5" />  
                              <xs:maxInclusive value="1440" />  
                            </xs:restriction>  
                          </xs:simpleType>  
                        </xs:element>  
  
           <!-- the default value is 128 entries -->

                        <xs:element name="PMKCacheSize" minOccurs="0">  
                          <xs:simpleType>  
                            <xs:restriction base="xs:integer">  
                              <xs:minInclusive value="1" />  
                              <xs:maxInclusive value="255" />  
                            </xs:restriction>  
                          </xs:simpleType>  
                        </xs:element>  
  
           <!-- the default value is "disabled" -->

                        <xs:element name="preAuthMode" minOccurs="0">  
                          <xs:simpleType>  
                            <xs:restriction base="xs:string">  
                              <xs:enumeration value="disabled" />  
                              <xs:enumeration value="enabled" />  
                            </xs:restriction>  
                          </xs:simpleType>  
                        </xs:element>  

           <!-- the default value is 3 times -->
                        <xs:element name="preAuthThrottle" minOccurs="0">  
                          <xs:simpleType>  
                            <xs:restriction base="xs:integer">  
                              <xs:minInclusive value="1" />  
                              <xs:maxInclusive value="16" />  
                            </xs:restriction>  
                          </xs:simpleType>  
                        </xs:element>  
  
           <!-- extension point for other namespaces -->
           <!-- this is the insertion point for OneX and HotspotAuth namespaces -->

                        <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />  
                      </xs:sequence>  
                    </xs:complexType>  
                  </xs:element>  

           <!-- extension point for other namespaces -->
               
                  <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />  
                </xs:sequence>  
              </xs:complexType>  
            </xs:element>  
  
    </xs:sequence>  
    <xs:attribute name="Priority" type="base:Priority" default="5"/>  
  </xs:complexType>  
  
  <xs:element name="WLANProfile" type="CarrierWLANProfile"/>  
</xs:schema>  

    <!-- provisioning_wlan_v2 -->
    <!-- The following shows the new elements in version 2  that can be included -->
 
<?xml version="1.0" encoding="utf-8"?>
<xs:schema targetNamespace="http://www.microsoft.com/networking/CarrierControl/WLAN/v2"
    elementFormDefault="qualified"
    xmlns="http://www.microsoft.com/networking/CarrierControl/WLAN/v2"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
>

  <xs:element name="SSID">
    <xs:complexType>
      <!-- Either Hex or named SSID must be present. -->
      <xs:choice>
        <xs:element name="hex">
          <xs:simpleType>
            <xs:restriction base="xs:hexBinary">
              <xs:minLength value="1" />
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
      </xs:choice>
    </xs:complexType>
  </xs:element>

  <xs:element name="SSIDPrefix">
    <xs:complexType>
      <!-- Either Hex or named SSID must be present. -->
      <xs:choice>
        <xs:element name="hex">
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
              <xs:minLength value="4" />
              <xs:maxLength value="32" />
            </xs:restriction>
          </xs:simpleType>
        </xs:element>
      </xs:choice>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

## Related topics


[**SSIDPrefix**](https://msdn.microsoft.com/library/windows/apps/dn297316)

[WLAN\_v2 schema](https://msdn.microsoft.com/library/windows/apps/dn297323)

 

 



