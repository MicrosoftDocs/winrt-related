---
title: DUSM schema
description: The Data Usage Subscription Management (DUSM) schema defines elements that are used to describe cost information for a subscriber's connection to a metered network.
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# DUSM schema


The Data Usage Subscription Management (DUSM) schema defines elements that are used to describe cost information for a subscriber's connection to a metered network. All of the elements are in the namespace `http://www.microsoft.com/networking/CarrierControl/DUSM/v1`. Not all elements are in every profile, as some elements are optional.

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
<td><a href="element-bandwidthinkbps.md">BandwidthInKbps</a> </td>
<td><p>Defines a value representing the effective link speed of the subscriber’s connection specified in Kbps. Must be a value from 0 to 2<sup>32nd</sup>.</p></td>
</tr>
<tr class="even">
<td><a href="element-billingcycle.md">BillingCycle</a> </td>
<td><p>Defines the plan's starting date and time, its duration, and what happens at the end of the billing cycle.</p></td>
</tr>
<tr class="odd">
<td><a href="element-carrierpolicy.md">CarrierPolicy</a> </td>
<td><p>Defines optional setting for Windows on this connection.</p></td>
</tr>
<tr class="even">
<td><a href="element-cost.md">Cost</a> </td>
<td><p>Defines a set of meter cost information that specifies the metered state of a subscriber's connection to a Mobile Network Operator (MNO). <a href="element-cost.md"><strong>Cost</strong></a>  is the unique root element for DUSM cost information.</p></td>
</tr>
<tr class="odd">
<td><a href="element-datalimitinmegabytes.md">DataLimitInMegabytes</a> </td>
<td><p>Defines a value representing the data limit in MB for a capped plan. Must be a value from 0 to 2<sup>32nd</sup>.</p></td>
</tr>
<tr class="even">
<td><a href="element-maxdownloadfilesizeinmegabytes.md">MaxDownloadFileSizeInMegabytes</a> </td>
<td><p>Defines a value representing the maximum suggested download size in MB of the subscriber's connection. Must be a value from 0 to 2<sup>32nd</sup>.</p></td>
</tr>
<tr class="odd">
<td><a href="element-securityupdatesexempt.md">SecurityUpdatesExempt</a> </td>
<td><p>If <strong>true</strong>, the MNO advises Windows Update (WU) that security updates are exempt from being counted as data usage against the subscriber’s plan and WU will download all security patches when on a metered network. Otherwise, WU will only download zero-day patches and not all security updates when <strong>false</strong>.</p></td>
</tr>
<tr class="even">
<td><a href="element-usageinmegabytes.md">UsageInMegabytes</a> </td>
<td><p>Defines a value representing the data used to-date within the current billing cycle in MB. Must be a value from 0 to 2<sup>32nd</sup>.</p></td>
</tr>
<tr class="odd">
<td><a href="element-usersmsenabled.md">UserSMSEnabled</a> </td>
<td><p>Indicates whether the subscriber's service includes user-to-user SMS which must be delivered in near real-time. If <strong>true</strong>, Windows will employ less aggressive power management on the Mobile Broadband interface to allow SMS messages to arrive more quickly. If <strong>false</strong>, SMS messages will arrive when the PC is next active.</p></td>
</tr>
</tbody>
</table>

 

The full DUSM schema is below:

``` syntax
<?xml version="1.0" encoding="utf-8"?>
<xs:schema targetNamespace="http://www.microsoft.com/networking/CarrierControl/DUSM/v1"
    elementFormDefault="qualified"
    xmlns="http://www.microsoft.com/networking/CarrierControl/DUSM/v1"
    xmlns:xs="http://www.w3.org/2001/XMLSchema">

  <xs:simpleType name="PlanType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="Unrestricted"/>
      <xs:enumeration value="Fixed"/>
      <xs:enumeration value="Variable"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:complexType name="Subscription">
    <xs:sequence>
      <xs:element name="UsageInMegabytes" minOccurs="0">
        <xs:complexType>
          <xs:simpleContent>
            <xs:extension base="xs:nonNegativeInteger">
              <xs:attribute name="Timestamp" type="xs:dateTime" use="required"/>
            </xs:extension>
          </xs:simpleContent>
        </xs:complexType>
      </xs:element>
      <xs:element name="DataLimitInMegabytes" type="xs:positiveInteger" minOccurs="0"/>

      <xs:element name="BillingCycle" minOccurs="0">
        <xs:complexType>
          <xs:attribute name="StartDate" type="xs:dateTime" use="required"/>
          <xs:attribute name="Duration" use="required">
            <xs:simpleType>
              <xs:restriction base="xs:duration">
                <xs:minExclusive value="PT0S"/>
              </xs:restriction>
            </xs:simpleType>
          </xs:attribute>
          <xs:attribute name="Resets" type="xs:boolean" default="true"/>
        </xs:complexType>
      </xs:element>
      <xs:element name="BandwidthInKbps" type="xs:nonNegativeInteger" minOccurs="0"/>

      <xs:element name="MaxDownloadFileSizeInMegabytes" type="xs:positiveInteger" default="25" minOccurs="0"/>
      
      <xs:element name="CarrierPolicy" minOccurs="0">
        <xs:complexType>
          <xs:sequence>
            <xs:element name="SecurityUpdatesExempt" type="xs:boolean" default="false" minOccurs="0"/>
            <xs:element name="UserSMSEnabled" type="xs:boolean" default="true" minOccurs="0"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:sequence>
    <xs:attribute name="OverDataLimit" type="xs:boolean"/>
    <xs:attribute name="Congested" type="xs:boolean"/>
    <xs:attribute name="PlanType" use="required" type="PlanType"/>
  </xs:complexType>
  <xs:element name="Cost" type="Subscription"/>
</xs:schema>
```

 

 



