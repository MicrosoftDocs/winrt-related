---
title: com4:Class (in ManagedInProcessServer)
description: TBD
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:Class (in ManagedInProcessServer)



## Description
TBD



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
| ThreadingModel | TBD | One of the following values: "Both" , "STA" , "MTA" , "MainSTA" , "Neutral"| Yes |
| ImplementationClass | TBD | An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1| Yes |
| Virtualization | TBD | One of the following values: "enabled" , "disabled"| Yes |
| ProgId | TBD | An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1| Yes |
| VersionIndependentProgId | TBD | An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1| Yes |
| AutoConvertTo | TBD | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.| Yes |
| InsertableObject | TBD | Boolean.| Yes |
| ShortDisplayName | TBD | A string between 1 and 40 characters in length.| Yes |
| Id | TBD | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.| Yes |
| DisplayName | TBD | A string between 1 and 256 characters in length. This string is localizable.| Yes |



## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | http://schemas.microsoft.com/appx/manifest/com/windows10/4 |
