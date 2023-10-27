---
title: com4:InProcessServer
description: Registers an in-process server with one or many class registrations. (com4:InProcessServer).
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:InProcessServer

Registers an in-process server with one or many class registrations.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:InProcessServer\>**

## Syntax

```xml
<com4:InProcessServer
  Path = 'An optional string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *, ending with the case-insensitive file extension ".dll".' />

  <!-- Child elements -->
  Class
  InProcessServerDll
  ClassReference

</com4:InProcessServer>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Path** | The path to the DLL. | One of the following values: A string between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `"`, `|` `?`, or `*`, ending with the case-insensitive file extension `.dll`. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [Class](element-com4-inprocessserver-class.md) | Defines an in-process server class registration. |
| [InProcessServerDll](element-com4-inprocessserverdll.md) | Specifies the path and processor architecture of an in-process server DLL. |
| [ClassReference](element-com4-inprocessserver-classreference.md) | Specifies the class with which the registered in-process server is associated and sets registration details. |

### Parent elements

| Parent element | Description |
|-|-|
| [Extensions](element-1-extensions.md) | Defines one or more extensibility points for the app. |

## Examples

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
| Minimum OS Version | Windows 10 (Build 20348) |
