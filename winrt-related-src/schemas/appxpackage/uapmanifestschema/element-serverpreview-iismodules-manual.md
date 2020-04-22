---
Description: Declares an app extensibility point of type windows.iisModules.
Search.Product: eADQiWindows 10XVcnh
title: serverpreview:IisModules
ms.assetid: f1f28b61-2a61-4799-851c-a8f52cca16b7


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# serverpreview:IisModules


Declares an app extensibility point of type **windows.iisModules**. This element identifies one or more Internet Information Service (IIS) modules to install, update, or uninstall out-of-band on Nano Server.

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
<dd><b>&lt;serverpreview:IisModules&gt;</b></dd>
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
<serverpreview:IisModules>
  <!-- Child elements -->
  serverpreview:IisModule{1,100}
</serverpreview:IisModules>
```

**Key**

          {} specific range of occurrences

## Attributes and Elements


**Attributes**

None.

**Child Elements**

| Child Element                                                             | Description                                                                                                          |
|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [**serverpreview:IisModule**](element-serverpreview-iismodule-manual.md) | Identifies an Internet Information Service (IIS) module to install, update, or uninstall out-of-band on Nano Server. |

 

**Parent Elements**

| Parent Element                                                            | Description                                  |
|---------------------------------------------------------------------------|----------------------------------------------|
| [**serverpreview:Extension**](element-serverpreview-extension-manual.md) | Declares an extensibility point for the app. |

 

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
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/serverpreview/windows10` |

 

 

 



