---
Description: The CarrierControlSignatureSchema schema defines elements that are used to describe the signature appended to the provisioning file.
MS-HAID: CarrierControlSignatureSchema.Schema\_Root
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: CarrierControlSignatureSchema schema
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# CarrierControlSignatureSchema schema


The CarrierControlSignatureSchema schema defines elements that are used to describe the signature appended to the provisioning file. It is based on the [XML DSIG](http://www.w3.org/TR/xmldsig-core/) specification with only minor deviations that are explicitly described below. All of the elements are in the namespace http://www.w3.org/2000/09/xmldsig\#. Not all elements are in every profile, as some elements are optional.

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
<td>[CanonicalizationMethod](element-canonicalizationmethod.md)</td>
<td><p>Defines the canonicalization method applied to [<strong>SignedInfo</strong>](element-signedinfo.md) as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/). Must be of type Canonical XML.</p></td>
</tr>
<tr class="even">
<td>[DSAKeyValue](element-dsakeyvalue.md)</td>
<td><p>Defines a Digital Signature Algorithm (DSA) public key as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="odd">
<td>[DigestMethod](element-digestmethod.md)</td>
<td><p>Defines the algorithm used to generate [<strong>DigestValue</strong>](element-digestvalue.md) as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="even">
<td>[DigestValue](element-digestvalue.md)</td>
<td><p>Defines the digest value as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/). The algorithm used to generate [<strong>DigestValue</strong>](element-digestvalue.md) is defined in [<strong>DigestMethod</strong>](element-digestmethod.md).</p></td>
</tr>
<tr class="odd">
<td>[Exponent](element-exponent.md)</td>
<td><p>Defines the RSA public key exponent as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="even">
<td>[G](element-g.md)</td>
<td><p>Defines an integer with certain properties with respect to [<strong>P</strong>](element-p.md) and [<strong>Q</strong>](element-q.md) as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="odd">
<td>[HMACOutputLength](element-hmacoutputlength.md)</td>
<td><p>Defines the length, in bits, of the [<strong>SignatureValue</strong>](element-signaturevalue.md) element as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="even">
<td>[J](element-j.md)</td>
<td><p>Defines ([<strong>P</strong>](element-p.md) - 1) / [<strong>Q</strong>](element-q.md) as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="odd">
<td>[KeyInfo](element-keyinfo.md)</td>
<td><p>Defines all key information used to validate the signature as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="even">
<td>[KeyValue](element-keyvalue.md)</td>
<td><p>Defines a single public key as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="odd">
<td>[Modulus](element-modulus.md)</td>
<td><p>Defines the RSA public key modulus as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="even">
<td>[P](element-p.md)</td>
<td><p>Defines a prime modulus meeting the [DSAwithSHA1](http://www.w3.org/2000/09/xmldsig#dsa-sha1 ) requirements as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="odd">
<td>[PgenCounter](element-pgencounter.md)</td>
<td><p>Defines a Digital Signature Algorithm (DSA) prime generation counter as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="even">
<td>[Q](element-q.md)</td>
<td><p>Defines an integer in the range 2**159 &lt; [<strong>Q</strong>](element-q.md) &lt; 2**160 which is a prime divisor of [<strong>P</strong>](element-p.md)-1 as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="odd">
<td>[RSAKeyValue](element-rsakeyvalue.md)</td>
<td><p>Defines a RSA public key as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="even">
<td>[Reference](element-reference.md)</td>
<td><p>Defines a digest value, digest method, and transforms as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="odd">
<td>[Seed](element-seed.md)</td>
<td><p>Defines a Digital Signature Algorithm (DSA) prime generation seed as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="even">
<td>[Signature](element-signature.md)</td>
<td><p>Defines the root element of an [XML DSIG](http://www.w3.org/TR/xmldsig-core/) compliant signature. [<strong>Signature</strong>](element-signature.md) is the unique root element for a provisioning file signature.</p></td>
</tr>
<tr class="odd">
<td>[SignatureMethod](element-signaturemethod.md)</td>
<td><p>Defines the algorithm used to generate the signature thumbprint in [<strong>SignatureValue</strong>](element-signaturevalue.md) as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="even">
<td>[SignatureValue](element-signaturevalue.md)</td>
<td><p>Defines the signature thumbprint as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/). The algorithm used to generate [<strong>SignatureValue</strong>](element-signaturevalue.md) is defined in [<strong>SignatureMethod</strong>](element-signaturemethod.md).</p></td>
</tr>
<tr class="odd">
<td>[SignedInfo](element-signedinfo.md)</td>
<td><p>Defines all signed content within the signature as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="even">
<td>[Transform](element-transform.md)</td>
<td><p>Defines a transform applied to the digested data object prior to [<strong>DigestMethod</strong>](element-digestmethod.md) as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="odd">
<td>[Transforms](element-transforms.md)</td>
<td><p>Defines a an ordered list of transforms applied to the digested data object as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="even">
<td>[X509Certificate](element-x509certificate.md)</td>
<td><p>Defines an X.509 compliant signature as defined in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="odd">
<td>[X509Data](element-x509data.md)</td>
<td><p>Defines one or more X.509 compliant signatures as defined in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
<tr class="even">
<td>[Y](element-y.md)</td>
<td><p>Defines [<strong>G</strong>](element-g.md)**X mod [<strong>P</strong>](element-p.md) (where X is part of the private key and not made public) as specified in [XML DSIG](http://www.w3.org/TR/xmldsig-core/).</p></td>
</tr>
</tbody>
</table>

 

The full CarrierControlSignatureSchema schema is below:

``` syntax
<?xml version="1.0" encoding="utf-8"?>  
  
<schema xmlns="http://www.w3.org/2001/XMLSchema"  
        xmlns:ds="http://www.w3.org/2000/09/xmldsig#"  
        targetNamespace="http://www.w3.org/2000/09/xmldsig#"  
        version="0.1" elementFormDefault="qualified">
  
<simpleType name="CryptoBinary">  
  <restriction base="base64Binary">  
  </restriction>  
</simpleType> 
  
<element name="Signature" type="ds:SignatureType"/>  
<complexType name="SignatureType">  
  <sequence>   
    <element ref="ds:SignedInfo"/>   
    <element ref="ds:SignatureValue"/>   
    <element ref="ds:KeyInfo" minOccurs="0"/>   
  </sequence>    
  <attribute name="Id" type="ID" use="optional"/>  
</complexType>  
  
  <element name="SignatureValue" type="ds:SignatureValueType"/>   
  <complexType name="SignatureValueType">  
    <simpleContent>  
      <extension base="base64Binary">  
        <attribute name="Id" type="ID" use="optional"/>  
      </extension>  
    </simpleContent>  
  </complexType>  
  
<element name="SignedInfo" type="ds:SignedInfoType"/>  
<complexType name="SignedInfoType">  
  <sequence>   
    <element ref="ds:CanonicalizationMethod"/>   
    <element ref="ds:SignatureMethod"/>   
    <element ref="ds:Reference"/>   
  </sequence>    
  <attribute name="Id" type="ID" use="optional"/>   
</complexType>  
  
  <element name="CanonicalizationMethod" type="ds:CanonicalizationMethodType"/>   
  <complexType name="CanonicalizationMethodType" mixed="true">  
    <attribute name="Algorithm" use="required">   
      <simpleType>  
        <restriction base="anyURI">  
          <enumeration value="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"/>  
          <enumeration value="http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments"/>  
          <enumeration value="http://www.w3.org/2001/10/xml-exc-c14n#"/>  
          <enumeration value="http://www.w3.org/2001/10/xml-exc-c14n#WithComments"/>  
        </restriction>  
      </simpleType>  
    </attribute>  
  </complexType>  
  
  <element name="SignatureMethod" type="ds:SignatureMethodType"/>  
  <complexType name="SignatureMethodType" mixed="true">  
    <sequence>  
      <element name="HMACOutputLength" minOccurs="0" type="ds:HMACOutputLengthType"/>  
      <any namespace="##other" minOccurs="0" maxOccurs="unbounded"/>   
    </sequence>  
    <attribute name="Algorithm" type="anyURI" use="required"/>   
  </complexType>  
  
<element name="Reference" type="ds:ReferenceType"/>  
<complexType name="ReferenceType">  
  <sequence>   
    <element ref="ds:Transforms"/>   
    <element ref="ds:DigestMethod"/>   
    <element ref="ds:DigestValue"/>   
  </sequence>  
  <attribute name="Id" type="ID" use="optional"/>    
  <attribute name="URI">  
    <simpleType>  
      <restriction base="anyURI">  
        <maxLength value="0"/>  
      </restriction>        
    </simpleType>  
  </attribute>  
</complexType>  
  
  <element name="Transforms" type="ds:TransformsType"/>  
  <complexType name="TransformsType">  
    <sequence>  
      <element ref="ds:Transform" maxOccurs="1"/>    
    </sequence>  
  </complexType>  
  
  <element name="Transform" type="ds:TransformType"/>  
  <complexType name="TransformType" mixed="true">  
    <attribute name="Algorithm" use="required">   
      <simpleType>  
        <restriction base="anyURI">  
          <enumeration value="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>  
        </restriction>  
      </simpleType>  
    </attribute>  
  </complexType>  
  
<element name="DigestMethod" type="ds:DigestMethodType"/>  
<complexType name="DigestMethodType" mixed="true">   
  <sequence>  
    <any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>  
  </sequence>      
  <attribute name="Algorithm" type="anyURI" use="required"/>   
</complexType>  
  
<element name="DigestValue" type="ds:DigestValueType"/>  
<simpleType name="DigestValueType">  
  <restriction base="base64Binary"/>  
</simpleType>  
  
<element name="KeyInfo" type="ds:KeyInfoType"/>   
<complexType name="KeyInfoType" mixed="true">  
  <choice maxOccurs="unbounded">       
    <element ref="ds:KeyValue"/>   
    <element ref="ds:X509Data"/>   
    <any processContents="lax" namespace="##other"/> 
  </choice>  
  <attribute name="Id" type="ID" use="optional"/>   
</complexType>  
  
  
  <element name="KeyValue" type="ds:KeyValueType"/>   
  <complexType name="KeyValueType" mixed="true">  
   <choice>  
     <element ref="ds:DSAKeyValue"/>  
     <element ref="ds:RSAKeyValue"/>  
     <any namespace="##other" processContents="lax"/>  
   </choice>  
  </complexType>  

<element name="X509Data" type="ds:X509DataType"/>   
<complexType name="X509DataType">  
  <sequence maxOccurs="unbounded">  
    <choice>  
      <element name="X509Certificate" type="base64Binary"/>  
    </choice>  
  </sequence>  
</complexType>  

<simpleType name="HMACOutputLengthType">  
  <restriction base="integer"/>  
</simpleType>  
  
<element name="DSAKeyValue" type="ds:DSAKeyValueType"/>  
<complexType name="DSAKeyValueType">  
  <sequence>  
    <sequence minOccurs="0">  
      <element name="P" type="ds:CryptoBinary"/>  
      <element name="Q" type="ds:CryptoBinary"/>  
    </sequence>  
    <element name="G" type="ds:CryptoBinary" minOccurs="0"/>  
    <element name="Y" type="ds:CryptoBinary"/>  
    <element name="J" type="ds:CryptoBinary" minOccurs="0"/>  
    <sequence minOccurs="0">  
      <element name="Seed" type="ds:CryptoBinary"/>  
      <element name="PgenCounter" type="ds:CryptoBinary"/>  
    </sequence>  
  </sequence>  
</complexType>  
  
<element name="RSAKeyValue" type="ds:RSAKeyValueType"/>  
<complexType name="RSAKeyValueType">  
  <sequence>  
    <element name="Modulus" type="ds:CryptoBinary"/>   
    <element name="Exponent" type="ds:CryptoBinary"/>   
  </sequence>  
</complexType>   
</schema>  
```

 

 



