---
title: com4:Class (in com4:ManagedInProcessServer)
description: Registers a managed in-process server with one or more classes. (in com4:ManagedInProcessServer)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:Class (in ManagedInProcessServer)



## Description
Registers a managed in-process server with one or more classes.


## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl><dt><a href = "element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl><dt><a href = "element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl><dt><a href = "element-com4-managedinprocessserver.md">&lt;com4:ManagedInProcessServer&gt;</a></dt>
<dd>
<b>&lt;com4:Class&gt;</b>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<com4:Class     ThreadingModel = "Both" | "STA" | "MTA" | "MainSTA" | "Neutral"
    ImplementationClass = An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1
    Virtualization = "enabled" | "disabled"
    ProgId = An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1
    VersionIndependentProgId = An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1
    AutoConvertTo = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
    InsertableObject = Boolean.
    ShortDisplayName = A string between 1 and 40 characters in length.
    Id = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
    DisplayName = A string between 1 and 256 characters in length. This string is localizable.
></com4:Class>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| ThreadingModel | The threading model for loading DLLs. | One of the following values: "Both" , "STA" , "MTA" , "MainSTA" , "Neutral"| Yes |
| ImplementationClass | The implementation class associated with the class reference. | An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1| Yes |
| Virtualization | Specifies whether virtualization is used when loading the class. | One of the following values: "enabled" , "disabled"| Yes |
| ProgId | Associates a programmatic identifier (ProgID) with a CLSID. | An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1| Yes |
| VersionIndependentProgId | Associates a ProgID with a CLSID. This value is used to determine the latest version of an object application. | An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1| Yes |
| AutoConvertTo | Specifies the automatic conversion of a given class of objects to a new class of objects. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.| Yes |
| InsertableObject | Indicates that this class is insertable. | Boolean.| Yes |
| ShortDisplayName | A short version of the class display name. | A string between 1 and 40 characters in length.| Yes |
| Id | The Id attribute corresponds to the CLSID. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.| Yes |
| DisplayName | A localizable string corresponding to the default value of the CLSID's key. | A string between 1 and 256 characters in length. This string is localizable.| Yes |

## Remarks

The following example shows the registration of multiple class implementations with a managed in-process server.

```xml
<com4:ManagedInProcessServer Assembly="Fabrikam.Widgets, Version=10.0.0.0, Culture=neutral, PublicKeyToken=xxxxxxxxxxxxxxxxx" RuntimeVersion="v4.0.30319"> 
  <com4:Class Id="99b9b8fa-2c14-42f7-xxxx-xxxxxxxxxxxx" DisplayName="SimpleWidget" ImplementationClass="Fabrikam.Widgets.SimpleWidget"/> 
  <com4:Class Id="0057c8be-3c95-4242-xxxx-xxxxxxxxxxxx" DisplayName="SingleThreadedWidget" ImplementationClass="Fabrikam.Widgets.SingleThreadedWidget" ThreadingModel="Apartment"/> 
</com4:ManagedInProcessServer> 
```

## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
