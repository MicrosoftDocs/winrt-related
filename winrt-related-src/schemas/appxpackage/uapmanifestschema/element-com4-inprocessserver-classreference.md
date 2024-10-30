---
title: com4:ClassReference (in InProcessServer)
description: Specifies the class with which the registered in-process server is associated and sets registration details. (in com4:InProcessServer)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:ClassReference (in InProcessServer)

Specifies the class with which the registered in-process server is associated and sets registration details.

## Element Hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:InProcessServer\>](element-com4-inprocessserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:ClassReference\>**

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:InProcessServer\>](element-com4-inprocessserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:ClassReference\>**

## Syntax

```xml
<com4:ClassReference
    ThreadingModel = 'A string that can have one of the following values: "Both", "STA", "MTA", "MainSTA", or "Neutral".'
    Virtualization = 'A string that can have one of the following values: "enabled" or "disabled".'
    Id = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ThreadingModel** | The type of threading model supported by the runtime class. | One of the following values: "Both" , "STA" , "MTA" , "MainSTA" , "Neutral"| Yes |  |
| **Virtualization** | Specifies whether virtualization is used when loading the class. | One of the following values: "enabled" , "disabled"| Yes |  |
| **Id** | The Id of the [Class](element-com4-class.md) being referenced. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.| Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [com4:InProcessServer](element-com4-inprocessserver.md) | Registers an in-process server with one or many class registrations. |

## Remarks

The following example shows how to register an out-of-process and an in-process server implementation for the same class.

```xml
<com4:Class Id="f4ed7720-9b3a-44a4-xxxx-xxxxxxxxxxxx" DisplayName="CLSID_Foo"/> 
<com:ExeServer Executable="MyServer.exe" DisplayName="My server">  
  <com4:ClassReference Id="f4ed7720-9b3a-44a4-xxxx-xxxxxxxxxxxx"/>  
</com:ExeServer> 
<com4:InProcessServer Path="MyServer.dll">  
  <com4:ClassReference Id="f4ed7720-9b3a-44a4-xxxx-xxxxxxxxxxxx"/>  
</com4:InProcessServer> 

```

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
| **Minimum OS Version** | Windows 10 (Build 20348) |
