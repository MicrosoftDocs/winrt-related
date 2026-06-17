---
title: uap2:Verb
description: Defines the verbs associated with a file context menu (uap2:Verb).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, uap2:Extension, uap2:FileTypeAssociation, uap2:SupportedVerbs, uap2:Verb]
---

# uap2:Verb

Defines the verbs associated with a file context menu and enables Windows Desktop Bridge apps to use ddeexec to launch.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap2:Extension>`](element-uap2-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap2:FileTypeAssociation>`](element-uap-filetypeassociation.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap2:SupportedVerbs>`](element-uap2-supportedverbs.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap2:Verb>`**  

## Syntax

```xml
<uap2:Verb
  Id = 'A required string with a value between 1 and 64 characters in length that consists of alphanumeric characters, periods (`.`), dashes (`-`), and spaces only.'
  Extended = 'An optional boolean value.'
  uap7:Default = 'An optional boolean value.'
  rescap3:DdeExecCommand = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  rescap3:DdeExecApplication = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  rescap3:DdeExecTopic = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  rescap3:DdeExecIfExec = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Id** | The name of the verb. | A string with a value between 1 and 64 characters in length that consists of alphanumeric characters, periods (`.`), dashes (`-`), and spaces only. | Yes |  |
| **Extended** | Specifies that the verb should only appear if the user holds the *Shift* key before right-clicking the file to show the context menu. | An optional boolean value. | No |  |
| **uap7:Default** | Specifies whether the verb is the default verb. Only one verb within **SupportedVerbs** can be set as the default verb. | An optional boolean value. | No |  |
| **rescap3:DdeExecCommand** | A DDE command string. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **rescap3:DdeExecApplication** | An application name used to establish the DDE conversion. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **rescap3:DdeExecTopic** | The topic name of the DDE conversion. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **rescap3:DdeExecIfExec** | The DDE command used if DDE conversion cannot be executed. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap2:SupportedVerbs](element-uap2-supportedverbs.md) | Contains verbs for a file context menu. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/2` |
| **rescap3** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/3` |
| **uap7** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/7` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
