---
Description: Identifies an Internet Information Service (IIS) SectionDefinition as it pertains to a same-named XML element in an applicationHost.config file.
Search.Product: eADQiWindows 10XVcnh
title: serverpreview:SectionDefinition
ms.assetid: 7fa268e0-a5aa-49d4-a37d-6be0a9ec6dda
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/2017
---

# serverpreview:SectionDefinition


Identifies an Internet Information Service (IIS) SectionDefinition as it pertains to a same-named XML element in an applicationHost.config file. The iisModule being installed claims ownership of this SectionDefinition inside the applicationHost.config file and in the corresponding SectionGroupDefinition hierarchy of the IIS instance that is installed on the target machine. If this SectionDefinition is defined at the root level, not inside a SectionGroupDefinition, and already exists at that level, installation is blocked.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-serverpreview-extension-manual.md">&lt;serverpreview:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-serverpreview-iismodules-manual.md">&lt;serverpreview:IisModules&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-serverpreview-iismodule-manual.md">&lt;serverpreview:IisModule&gt;</a></dt>
<dd><b>&lt;serverpreview:SectionDefinition&gt;</b></dd>
<dd>
<dl>
<dt><a href="element-serverpreview-sectiondata-manual.md">&lt;serverpreview:SectionData&gt;</a></dt>
<dd><b>&lt;serverpreview:SectionDefinition&gt;</b></dd>
<dl>									
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
</dd>
</dl>
</dd>
</dl>

## Syntax


```
<serverpreview:SectionDefinition Name                 = A string between 1 and 
                                                        32767 characters in 
                                                        length with a non-
                                                        whitespace character at 
                                                        its beginning and end. 
                                 OverrideModeDefault? = "allow" | "deny"
                                 AllowDefinition?     = "machineonly" | 
                                                        "machineToRootWeb" | 
                                                        "appHostOnly" |
                                                        "machineToApplication" |
                                                        "everywhere" >
</serverpreview:SectionDefintion>
```

**Key**

          \* optional (zero or more)

## Attributes and Elements


**Attributes**

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
<th>Data type</th>
<th>Required</th>
<th>Default value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Name</strong></td>
<td>The name of the SectionDefinition.</td>
<td>A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>OverrideModeDefault</strong></td>
<td>Specifies whether or not this section is locked by default. Unlocked sections can further be delegated to site or application level by the IIS administrators after the installation.</td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>allow</li>
<li>deny</li>
</ul></td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>AllowDefinition</strong></td>
<td>Indicates where in the configuration file hierarchy this section can be defined.</td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>machineOnly</li>
<li>machineToRootWeb</li>
<li>appHostOnly</li>
<li>machineToApplication</li>
<li>everywhere</li>
</ul></td>
<td>No</td>
<td>everywhere</td>
</tr>
</tbody>
</table>

 

**Child Elements**

None.

**Parent Elements**

| Parent Element                                                                                      | Description                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**serverpreview:IisModule**](element-serverpreview-iismodule-manual.md)                           | Identifies an Internet Information Service (IIS) module to install, update, or uninstall out-of-band on Nano Server.                                                                                                                                                                 |
| [**serverpreview:SectionGroupDefinition**](element-serverpreview-sectiongroupdefinition-manual.md) | Identifies an Internet Information Service (IIS) SectionGroupDefinition as it pertains to a same-named XML element in an applicationHost.config file. A SectionDefinition may be nested inside a hierarchy of one or more SectionGroupDefinitions. if not defined at the root level. |

 

## Examples


```XML
<Package ...
         xmlns:serverpreview=http://schemas.microsoft.com/appx/manifest/serverpreview/windows10"  
         IgnorableNamespaces="... serverpreview">
    <Applications>
        <Application>
            <Extensions>
                <serverpreview:Extension Category="windows.iisModules">  
                    <serverpreview:IisModules>  
                        <serverpreview:IisModule 
                                    Name="RewriteModule"  
                                    ModuleDll="rewrite.dll"  
                                    SchemaFileName="rewrite_schema.xml">  
                            <serverpreview:SectionGroupDefinition 
                                    Name="rewrite">  
                                <serverpreview:SectionDefinition 
                                    Name="rules"  
                                    OverrideModeDefault="allow"/>  
                                <serverpreview:SectionDefinition 
                                    Name="globalRules"  
                                    OverrideModeDefault="deny"                    
                                    AllowDefinition="appHostOnly"/>  
                                <serverpreview:SectionDefinition 
                                    Name="outboundRules"  
                                    OverrideModeDefault="allow"/>  
                                <serverpreview:SectionDefinition 
                                    Name="providers"  
                                    OverrideModeDefault="allow"/>  
                                <serverpreview:SectionDefinition 
                                    Name="rewriteMaps"  
                                    OverrideModeDefault="allow"/>  
                                <serverpreview:SectionDefinition 
                                    Name="allowedServerVariables"                          
                                    OverrideModeDefault="deny"/>  
                            </serverpreview:SectionGroupDefinition>  
                        </serverpreview:IisModule>  
                    </serverpreview:IisModules> 
                </serverpreview:Extension>  
            </Extensions>
        </Application>
    </Applications>
</Package>
```

## Requirements


|               |                                                                    |
|---------------|--------------------------------------------------------------------|
| **Namespace** | http://schemas.microsoft.com/appx/manifest/serverpreview/windows10 |

 

 

 



