<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Cómo instalar pnpm***

- ***npm** y **pnpm** son gestores de paquetes para Node.js. Aunque npm es el más conocido y utilizado, pnpm surgió poco después y se ha convertido en una alternativa popular debido a su eficiencia en la gestión de dependencias. Ambos gestores permiten inicializar un proyecto de Node.js con el comando `npm init`.*

## ***Inicialización de un proyecto con npm***

```bash
npm init
```

**Este comando te guiará a través de la creación de un fichero `package.json`. A continuación, se muestran los mensajes y las preguntas que el comando `npm init` te presentará:**

```bash
This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help init` for definitive documentation on these fields
and exactly what they do.

Use `npm install <pkg>` afterwards to install a package and
save it as a dependency in the package.json file.

Press ^C at any time to quit.
package name: (nodejs) nodejs
version: (1.0.0) 1.0.0
description: Guia Node.js
entry point: (index.js) index.js
test command: 
git repository: git@github.com:D4nitrix13/Node-JS.git
keywords: nodejs, node
author: Daniel Benjamin Perez Morales - D4nitrix13
license: (ISC) MIT
About to write to /home/d4nitrix13/Desktop/NodeJs/package.json:
```

**El resultado será un fichero `package.json` como el siguiente:**

```json
{
  "name": "nodejs",
  "version": "1.0.0",
  "description": "Guia Node.js",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "repository": {
    "type": "git",
    "url": "git+ssh://git@github.com/D4nitrix13/Node-JS.git"
  },
  "keywords": [
    "nodejs",
    "node"
  ],
  "author": "Daniel Benjamin Perez Morales - D4nitrix13",
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/D4nitrix13/Node-JS/issues"
  },
  "homepage": "https://github.com/D4nitrix13/Node-JS#readme"
}
```

- *Al finalizar, se te preguntará si todo está correcto, y puedes confirmar escribiendo "yes" o "Y".*

### ***Instalación de dependencias***

**Para instalar una dependencia, como el paquete [picocolors](https://www.npmjs.com/package/picocolors "https://www.npmjs.com/package/picocolors"), puedes usar el siguiente comando:**

```bash
npm install picocolors
```

**El resultado será algo similar a esto:**

```bash
npm i picocolors

added 1 package, and audited 2 packages in 2s

found 0 vulnerabilities
```

- *Para más información sobre el repositorio de picocolors, puedes visitar [este enlace](https://github.com/alexeyraspopov/picocolors "https://github.com/alexeyraspopov/picocolors").*

## ***Modificación del `package.json` al instalar una dependencia***

**Cuando instalas una dependencia, el fichero `package.json` se actualiza automáticamente. A continuación, se muestra un ejemplo de cómo se vería después de instalar `picocolors`:**

```json
{
  "name": "nodejs",
  "version": "1.0.0",
  "description": "Guía Node.js",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "repository": {
    "type": "git",
    "url": "git+ssh://git@github.com/D4nitrix13/Node-JS.git"
  },
  "keywords": [
    "nodejs",
    "node"
  ],
  "author": "Daniel Benjamin Perez Morales - D4nitrix13",
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/D4nitrix13/Node-JS/issues"
  },
  "homepage": "https://github.com/D4nitrix13/Node-JS#readme",
  "dependencies": {
    "picocolors": "1.0.1"
  }
}
```

**Además, se genera un fichero `package-lock.json` que asegura que las versiones de las dependencias sean consistentes. Aquí hay un ejemplo:**

```json
{
  "name": "nodejs",
  "version": "1.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "nodejs",
      "version": "1.0.0",
      "license": "MIT",
      "dependencies": {
        "picocolors": "1.0.1"
      }
    },
    "node_modules/picocolors": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/picocolors/-/picocolors-1.0.1.tgz",
      "integrity": "sha512-anP1Z8qwhkbmu7MFP5iTt+wQKXgwzf7zTyGlcdzabySa9vd0Xt392U0rVmz9poOaBj0uHJKyyo9/upk0HrEQew=="
    }
  }
}
```

### ***El operador `^` en las versiones de dependencias***

- *El operador `^`, llamado "caret", permite que npm instale cualquier versión compatible con la versión especificada, respetando las reglas de versionado semántico. Por ejemplo:*

```json
"picocolors": "^1.0.1"
```

- *Esto significa que npm instalará cualquier versión de `picocolors` que sea compatible con `1.x.x`, es decir, cualquier versión mayor o igual a `1.0.1` pero menor que `2.0.0`.*

- *No todas las dependencias se actualizan automáticamente. Para gestionar y actualizar las versiones de las dependencias, puedes usar la extensión Version Lens en Visual Studio Code. Esta extensión muestra la última versión disponible para cada paquete y te permite actualizar fácilmente las dependencias.*

```bash
"picocolors": "1.0.1"
```

### ***Instalación y uso de Version Lens***

```bash
Nombre: Version Lens
ID: pflannery.vscode-versionlens
Descripción: Shows the latest version for each package using code lens
Versión: 1.14.2
Editor: pflannery
Vínculo de VS Marketplace: https://marketplace.visualstudio.com/items?itemName=pflannery.vscode-versionlens
```

### ***Versionado semántico (SemVer)***

**El versionado semántico usa un formato `X.Y.Z`:**

- **X:** *`Major` - Cambios incompatibles con versiones anteriores.*
- **Y:** *`Minor` - Nuevas funcionalidades compatibles.*
- **Z:** *`Patch` - Correcciones de errores y mejoras menores.*

- *Por ejemplo, TypeScript a veces no sigue estrictamente el versionado semántico y puede introducir cambios incompatibles en versiones de parche (patch), lo que puede romper la compatibilidad con proyectos existentes.*

### ***Estructura del directorio `node_modules`***

**Al instalar un paquete, se crea un directorio llamado `node_modules` donde se almacenan las dependencias instaladas. Aquí hay un ejemplo de cómo se vería el contenido de este directorio después de instalar `picocolors`:**

```bash
tree -C ./node_modules/
./node_modules/
└── picocolors
    ├── LICENSE
    ├── package.json
    ├── picocolors.browser.js
    ├── picocolors.d.ts
    ├── picocolors.js
    ├── README.md
    └── types.ts

1 directory, 7 files
```

## ***Instalación de otros paquetes***

**Cuando instalamos otros paquetes, como `lodash`, npm creará un directorio con el nombre del paquete dentro del directorio `node_modules` y contendrá varios ficheros y subdirectorios. A continuación se muestra cómo se vería esto:**

### ***Instalación de lodash***

**Para instalar `lodash`, puedes usar el siguiente comando:**

```bash
npm install lodash
```

### ***Estructura del directorio node_modules***

**Después de instalar lodash, el directorio node_modules se verá algo así:**

```bash
[01;34m./node_modules/[0m
├── [01;34mlodash[0m
│   ├── add.js
│   ├── after.js
│   ├── _apply.js
│   ├── _arrayAggregator.js
│   ├── _arrayEach.js
│   ├── _arrayEachRight.js
│   ├── _arrayEvery.js
│   ├── _arrayFilter.js
│   ├── _arrayIncludes.js
│   ├── _arrayIncludesWith.js
│   ├── array.js
│   ├── _arrayLikeKeys.js
│   ├── _arrayMap.js
│   ├── _arrayPush.js
│   ├── _arrayReduce.js
│   ├── _arrayReduceRight.js
│   ├── _arraySample.js
│   ├── _arraySampleSize.js
│   ├── _arrayShuffle.js
│   ├── _arraySome.js
│   ├── ary.js
│   ├── _asciiSize.js
│   ├── _asciiToArray.js
│   ├── _asciiWords.js
│   ├── assignIn.js
│   ├── assignInWith.js
│   ├── assign.js
│   ├── _assignMergeValue.js
│   ├── _assignValue.js
│   ├── assignWith.js
│   ├── _assocIndexOf.js
│   ├── at.js
│   ├── attempt.js
│   ├── _baseAggregator.js
│   ├── _baseAssignIn.js
│   ├── _baseAssign.js
│   ├── _baseAssignValue.js
│   ├── _baseAt.js
│   ├── _baseClamp.js
│   ├── _baseClone.js
│   ├── _baseConforms.js
│   ├── _baseConformsTo.js
│   ├── _baseCreate.js
│   ├── _baseDelay.js
│   ├── _baseDifference.js
│   ├── _baseEach.js
│   ├── _baseEachRight.js
│   ├── _baseEvery.js
│   ├── _baseExtremum.js
│   ├── _baseFill.js
│   ├── _baseFilter.js
│   ├── _baseFindIndex.js
│   ├── _baseFindKey.js
│   ├── _baseFlatten.js
│   ├── _baseFor.js
│   ├── _baseForOwn.js
│   ├── _baseForOwnRight.js
│   ├── _baseForRight.js
│   ├── _baseFunctions.js
│   ├── _baseGetAllKeys.js
│   ├── _baseGet.js
│   ├── _baseGetTag.js
│   ├── _baseGt.js
│   ├── _baseHasIn.js
│   ├── _baseHas.js
│   ├── _baseIndexOf.js
│   ├── _baseIndexOfWith.js
│   ├── _baseInRange.js
│   ├── _baseIntersection.js
│   ├── _baseInverter.js
│   ├── _baseInvoke.js
│   ├── _baseIsArguments.js
│   ├── _baseIsArrayBuffer.js
│   ├── _baseIsDate.js
│   ├── _baseIsEqualDeep.js
│   ├── _baseIsEqual.js
│   ├── _baseIsMap.js
│   ├── _baseIsMatch.js
│   ├── _baseIsNaN.js
│   ├── _baseIsNative.js
│   ├── _baseIsRegExp.js
│   ├── _baseIsSet.js
│   ├── _baseIsTypedArray.js
│   ├── _baseIteratee.js
│   ├── _baseKeysIn.js
│   ├── _baseKeys.js
│   ├── _baseLodash.js
│   ├── _baseLt.js
│   ├── _baseMap.js
│   ├── _baseMatches.js
│   ├── _baseMatchesProperty.js
│   ├── _baseMean.js
│   ├── _baseMergeDeep.js
│   ├── _baseMerge.js
│   ├── _baseNth.js
│   ├── _baseOrderBy.js
│   ├── _basePickBy.js
│   ├── _basePick.js
│   ├── _basePropertyDeep.js
│   ├── _baseProperty.js
│   ├── _basePropertyOf.js
│   ├── _basePullAll.js
│   ├── _basePullAt.js
│   ├── _baseRandom.js
│   ├── _baseRange.js
│   ├── _baseReduce.js
│   ├── _baseRepeat.js
│   ├── _baseRest.js
│   ├── _baseSample.js
│   ├── _baseSampleSize.js
│   ├── _baseSetData.js
│   ├── _baseSet.js
│   ├── _baseSetToString.js
│   ├── _baseShuffle.js
│   ├── _baseSlice.js
│   ├── _baseSome.js
│   ├── _baseSortBy.js
│   ├── _baseSortedIndexBy.js
│   ├── _baseSortedIndex.js
│   ├── _baseSortedUniq.js
│   ├── _baseSum.js
│   ├── _baseTimes.js
│   ├── _baseToNumber.js
│   ├── _baseToPairs.js
│   ├── _baseToString.js
│   ├── _baseTrim.js
│   ├── _baseUnary.js
│   ├── _baseUniq.js
│   ├── _baseUnset.js
│   ├── _baseUpdate.js
│   ├── _baseValues.js
│   ├── _baseWhile.js
│   ├── _baseWrapperValue.js
│   ├── _baseXor.js
│   ├── _baseZipObject.js
│   ├── before.js
│   ├── bindAll.js
│   ├── bind.js
│   ├── bindKey.js
│   ├── _cacheHas.js
│   ├── camelCase.js
│   ├── capitalize.js
│   ├── castArray.js
│   ├── _castArrayLikeObject.js
│   ├── _castFunction.js
│   ├── _castPath.js
│   ├── _castRest.js
│   ├── _castSlice.js
│   ├── ceil.js
│   ├── chain.js
│   ├── _charsEndIndex.js
│   ├── _charsStartIndex.js
│   ├── chunk.js
│   ├── clamp.js
│   ├── _cloneArrayBuffer.js
│   ├── _cloneBuffer.js
│   ├── _cloneDataView.js
│   ├── cloneDeep.js
│   ├── cloneDeepWith.js
│   ├── clone.js
│   ├── _cloneRegExp.js
│   ├── _cloneSymbol.js
│   ├── _cloneTypedArray.js
│   ├── cloneWith.js
│   ├── collection.js
│   ├── commit.js
│   ├── compact.js
│   ├── _compareAscending.js
│   ├── _compareMultiple.js
│   ├── _composeArgs.js
│   ├── _composeArgsRight.js
│   ├── concat.js
│   ├── cond.js
│   ├── conforms.js
│   ├── conformsTo.js
│   ├── constant.js
│   ├── _copyArray.js
│   ├── _copyObject.js
│   ├── _copySymbolsIn.js
│   ├── _copySymbols.js
│   ├── core.js
│   ├── _coreJsData.js
│   ├── core.min.js
│   ├── countBy.js
│   ├── _countHolders.js
│   ├── _createAggregator.js
│   ├── _createAssigner.js
│   ├── _createBaseEach.js
│   ├── _createBaseFor.js
│   ├── _createBind.js
│   ├── _createCaseFirst.js
│   ├── _createCompounder.js
│   ├── _createCtor.js
│   ├── _createCurry.js
│   ├── _createFind.js
│   ├── _createFlow.js
│   ├── _createHybrid.js
│   ├── _createInverter.js
│   ├── create.js
│   ├── _createMathOperation.js
│   ├── _createOver.js
│   ├── _createPadding.js
│   ├── _createPartial.js
│   ├── _createRange.js
│   ├── _createRecurry.js
│   ├── _createRelationalOperation.js
│   ├── _createRound.js
│   ├── _createSet.js
│   ├── _createToPairs.js
│   ├── _createWrap.js
│   ├── curry.js
│   ├── curryRight.js
│   ├── _customDefaultsAssignIn.js
│   ├── _customDefaultsMerge.js
│   ├── _customOmitClone.js
│   ├── _DataView.js
│   ├── date.js
│   ├── debounce.js
│   ├── deburr.js
│   ├── _deburrLetter.js
│   ├── defaultsDeep.js
│   ├── defaults.js
│   ├── defaultTo.js
│   ├── defer.js
│   ├── _defineProperty.js
│   ├── delay.js
│   ├── differenceBy.js
│   ├── difference.js
│   ├── differenceWith.js
│   ├── divide.js
│   ├── drop.js
│   ├── dropRight.js
│   ├── dropRightWhile.js
│   ├── dropWhile.js
│   ├── each.js
│   ├── eachRight.js
│   ├── endsWith.js
│   ├── entriesIn.js
│   ├── entries.js
│   ├── eq.js
│   ├── _equalArrays.js
│   ├── _equalByTag.js
│   ├── _equalObjects.js
│   ├── _escapeHtmlChar.js
│   ├── escape.js
│   ├── escapeRegExp.js
│   ├── _escapeStringChar.js
│   ├── every.js
│   ├── extend.js
│   ├── extendWith.js
│   ├── fill.js
│   ├── filter.js
│   ├── findIndex.js
│   ├── find.js
│   ├── findKey.js
│   ├── findLastIndex.js
│   ├── findLast.js
│   ├── findLastKey.js
│   ├── first.js
│   ├── flake.lock
│   ├── flake.nix
│   ├── flatMapDeep.js
│   ├── flatMapDepth.js
│   ├── flatMap.js
│   ├── _flatRest.js
│   ├── flattenDeep.js
│   ├── flattenDepth.js
│   ├── flatten.js
│   ├── flip.js
│   ├── floor.js
│   ├── flow.js
│   ├── flowRight.js
│   ├── forEach.js
│   ├── forEachRight.js
│   ├── forIn.js
│   ├── forInRight.js
│   ├── forOwn.js
│   ├── forOwnRight.js
│   ├── [01;34mfp[0m
│   │   ├── add.js
│   │   ├── after.js
│   │   ├── all.js
│   │   ├── allPass.js
│   │   ├── always.js
│   │   ├── any.js
│   │   ├── anyPass.js
│   │   ├── apply.js
│   │   ├── array.js
│   │   ├── ary.js
│   │   ├── assignAll.js
│   │   ├── assignAllWith.js
│   │   ├── assignInAll.js
│   │   ├── assignInAllWith.js
│   │   ├── assignIn.js
│   │   ├── assignInWith.js
│   │   ├── assign.js
│   │   ├── assignWith.js
│   │   ├── assoc.js
│   │   ├── assocPath.js
│   │   ├── at.js
│   │   ├── attempt.js
│   │   ├── _baseConvert.js
│   │   ├── before.js
│   │   ├── bindAll.js
│   │   ├── bind.js
│   │   ├── bindKey.js
│   │   ├── camelCase.js
│   │   ├── capitalize.js
│   │   ├── castArray.js
│   │   ├── ceil.js
│   │   ├── chain.js
│   │   ├── chunk.js
│   │   ├── clamp.js
│   │   ├── cloneDeep.js
│   │   ├── cloneDeepWith.js
│   │   ├── clone.js
│   │   ├── cloneWith.js
│   │   ├── collection.js
│   │   ├── commit.js
│   │   ├── compact.js
│   │   ├── complement.js
│   │   ├── compose.js
│   │   ├── concat.js
│   │   ├── cond.js
│   │   ├── conforms.js
│   │   ├── conformsTo.js
│   │   ├── constant.js
│   │   ├── contains.js
│   │   ├── _convertBrowser.js
│   │   ├── convert.js
│   │   ├── countBy.js
│   │   ├── create.js
│   │   ├── curry.js
│   │   ├── curryN.js
│   │   ├── curryRight.js
│   │   ├── curryRightN.js
│   │   ├── date.js
│   │   ├── debounce.js
│   │   ├── deburr.js
│   │   ├── defaultsAll.js
│   │   ├── defaultsDeepAll.js
│   │   ├── defaultsDeep.js
│   │   ├── defaults.js
│   │   ├── defaultTo.js
│   │   ├── defer.js
│   │   ├── delay.js
│   │   ├── differenceBy.js
│   │   ├── difference.js
│   │   ├── differenceWith.js
│   │   ├── dissoc.js
│   │   ├── dissocPath.js
│   │   ├── divide.js
│   │   ├── drop.js
│   │   ├── dropLast.js
│   │   ├── dropLastWhile.js
│   │   ├── dropRight.js
│   │   ├── dropRightWhile.js
│   │   ├── dropWhile.js
│   │   ├── each.js
│   │   ├── eachRight.js
│   │   ├── endsWith.js
│   │   ├── entriesIn.js
│   │   ├── entries.js
│   │   ├── eq.js
│   │   ├── equals.js
│   │   ├── escape.js
│   │   ├── escapeRegExp.js
│   │   ├── every.js
│   │   ├── extendAll.js
│   │   ├── extendAllWith.js
│   │   ├── extend.js
│   │   ├── extendWith.js
│   │   ├── _falseOptions.js
│   │   ├── fill.js
│   │   ├── filter.js
│   │   ├── findFrom.js
│   │   ├── findIndexFrom.js
│   │   ├── findIndex.js
│   │   ├── find.js
│   │   ├── findKey.js
│   │   ├── findLastFrom.js
│   │   ├── findLastIndexFrom.js
│   │   ├── findLastIndex.js
│   │   ├── findLast.js
│   │   ├── findLastKey.js
│   │   ├── first.js
│   │   ├── F.js
│   │   ├── flatMapDeep.js
│   │   ├── flatMapDepth.js
│   │   ├── flatMap.js
│   │   ├── flattenDeep.js
│   │   ├── flattenDepth.js
│   │   ├── flatten.js
│   │   ├── flip.js
│   │   ├── floor.js
│   │   ├── flow.js
│   │   ├── flowRight.js
│   │   ├── forEach.js
│   │   ├── forEachRight.js
│   │   ├── forIn.js
│   │   ├── forInRight.js
│   │   ├── forOwn.js
│   │   ├── forOwnRight.js
│   │   ├── fromPairs.js
│   │   ├── function.js
│   │   ├── functionsIn.js
│   │   ├── functions.js
│   │   ├── get.js
│   │   ├── getOr.js
│   │   ├── groupBy.js
│   │   ├── gte.js
│   │   ├── gt.js
│   │   ├── hasIn.js
│   │   ├── has.js
│   │   ├── head.js
│   │   ├── identical.js
│   │   ├── identity.js
│   │   ├── includesFrom.js
│   │   ├── includes.js
│   │   ├── indexBy.js
│   │   ├── indexOfFrom.js
│   │   ├── indexOf.js
│   │   ├── initial.js
│   │   ├── init.js
│   │   ├── inRange.js
│   │   ├── intersectionBy.js
│   │   ├── intersection.js
│   │   ├── intersectionWith.js
│   │   ├── invertBy.js
│   │   ├── invert.js
│   │   ├── invertObj.js
│   │   ├── invokeArgs.js
│   │   ├── invokeArgsMap.js
│   │   ├── invoke.js
│   │   ├── invokeMap.js
│   │   ├── isArguments.js
│   │   ├── isArrayBuffer.js
│   │   ├── isArray.js
│   │   ├── isArrayLike.js
│   │   ├── isArrayLikeObject.js
│   │   ├── isBoolean.js
│   │   ├── isBuffer.js
│   │   ├── isDate.js
│   │   ├── isElement.js
│   │   ├── isEmpty.js
│   │   ├── isEqual.js
│   │   ├── isEqualWith.js
│   │   ├── isError.js
│   │   ├── isFinite.js
│   │   ├── isFunction.js
│   │   ├── isInteger.js
│   │   ├── isLength.js
│   │   ├── isMap.js
│   │   ├── isMatch.js
│   │   ├── isMatchWith.js
│   │   ├── isNaN.js
│   │   ├── isNative.js
│   │   ├── isNil.js
│   │   ├── isNull.js
│   │   ├── isNumber.js
│   │   ├── isObject.js
│   │   ├── isObjectLike.js
│   │   ├── isPlainObject.js
│   │   ├── isRegExp.js
│   │   ├── isSafeInteger.js
│   │   ├── isSet.js
│   │   ├── isString.js
│   │   ├── isSymbol.js
│   │   ├── isTypedArray.js
│   │   ├── isUndefined.js
│   │   ├── isWeakMap.js
│   │   ├── isWeakSet.js
│   │   ├── iteratee.js
│   │   ├── join.js
│   │   ├── __.js
│   │   ├── juxt.js
│   │   ├── kebabCase.js
│   │   ├── keyBy.js
│   │   ├── keysIn.js
│   │   ├── keys.js
│   │   ├── lang.js
│   │   ├── lastIndexOfFrom.js
│   │   ├── lastIndexOf.js
│   │   ├── last.js
│   │   ├── lowerCase.js
│   │   ├── lowerFirst.js
│   │   ├── lte.js
│   │   ├── lt.js
│   │   ├── map.js
│   │   ├── mapKeys.js
│   │   ├── _mapping.js
│   │   ├── mapValues.js
│   │   ├── matches.js
│   │   ├── matchesProperty.js
│   │   ├── math.js
│   │   ├── maxBy.js
│   │   ├── max.js
│   │   ├── meanBy.js
│   │   ├── mean.js
│   │   ├── memoize.js
│   │   ├── mergeAll.js
│   │   ├── mergeAllWith.js
│   │   ├── merge.js
│   │   ├── mergeWith.js
│   │   ├── method.js
│   │   ├── methodOf.js
│   │   ├── minBy.js
│   │   ├── min.js
│   │   ├── mixin.js
│   │   ├── multiply.js
│   │   ├── nAry.js
│   │   ├── negate.js
│   │   ├── next.js
│   │   ├── noop.js
│   │   ├── now.js
│   │   ├── nthArg.js
│   │   ├── nth.js
│   │   ├── number.js
│   │   ├── object.js
│   │   ├── omitAll.js
│   │   ├── omitBy.js
│   │   ├── omit.js
│   │   ├── once.js
│   │   ├── orderBy.js
│   │   ├── overArgs.js
│   │   ├── overEvery.js
│   │   ├── over.js
│   │   ├── overSome.js
│   │   ├── padCharsEnd.js
│   │   ├── padChars.js
│   │   ├── padCharsStart.js
│   │   ├── padEnd.js
│   │   ├── pad.js
│   │   ├── padStart.js
│   │   ├── parseInt.js
│   │   ├── partial.js
│   │   ├── partialRight.js
│   │   ├── partition.js
│   │   ├── pathEq.js
│   │   ├── path.js
│   │   ├── pathOr.js
│   │   ├── paths.js
│   │   ├── pickAll.js
│   │   ├── pickBy.js
│   │   ├── pick.js
│   │   ├── pipe.js
│   │   ├── placeholder.js
│   │   ├── plant.js
│   │   ├── pluck.js
│   │   ├── propEq.js
│   │   ├── property.js
│   │   ├── propertyOf.js
│   │   ├── prop.js
│   │   ├── propOr.js
│   │   ├── props.js
│   │   ├── pullAllBy.js
│   │   ├── pullAll.js
│   │   ├── pullAllWith.js
│   │   ├── pullAt.js
│   │   ├── pull.js
│   │   ├── random.js
│   │   ├── range.js
│   │   ├── rangeRight.js
│   │   ├── rangeStep.js
│   │   ├── rangeStepRight.js
│   │   ├── rearg.js
│   │   ├── reduce.js
│   │   ├── reduceRight.js
│   │   ├── reject.js
│   │   ├── remove.js
│   │   ├── repeat.js
│   │   ├── replace.js
│   │   ├── restFrom.js
│   │   ├── rest.js
│   │   ├── result.js
│   │   ├── reverse.js
│   │   ├── round.js
│   │   ├── sample.js
│   │   ├── sampleSize.js
│   │   ├── seq.js
│   │   ├── set.js
│   │   ├── setWith.js
│   │   ├── shuffle.js
│   │   ├── size.js
│   │   ├── slice.js
│   │   ├── snakeCase.js
│   │   ├── some.js
│   │   ├── sortBy.js
│   │   ├── sortedIndexBy.js
│   │   ├── sortedIndex.js
│   │   ├── sortedIndexOf.js
│   │   ├── sortedLastIndexBy.js
│   │   ├── sortedLastIndex.js
│   │   ├── sortedLastIndexOf.js
│   │   ├── sortedUniqBy.js
│   │   ├── sortedUniq.js
│   │   ├── split.js
│   │   ├── spreadFrom.js
│   │   ├── spread.js
│   │   ├── startCase.js
│   │   ├── startsWith.js
│   │   ├── string.js
│   │   ├── stubArray.js
│   │   ├── stubFalse.js
│   │   ├── stubObject.js
│   │   ├── stubString.js
│   │   ├── stubTrue.js
│   │   ├── subtract.js
│   │   ├── sumBy.js
│   │   ├── sum.js
│   │   ├── symmetricDifferenceBy.js
│   │   ├── symmetricDifference.js
│   │   ├── symmetricDifferenceWith.js
│   │   ├── tail.js
│   │   ├── take.js
│   │   ├── takeLast.js
│   │   ├── takeLastWhile.js
│   │   ├── takeRight.js
│   │   ├── takeRightWhile.js
│   │   ├── takeWhile.js
│   │   ├── tap.js
│   │   ├── template.js
│   │   ├── templateSettings.js
│   │   ├── throttle.js
│   │   ├── thru.js
│   │   ├── times.js
│   │   ├── T.js
│   │   ├── toArray.js
│   │   ├── toFinite.js
│   │   ├── toInteger.js
│   │   ├── toIterator.js
│   │   ├── toJSON.js
│   │   ├── toLength.js
│   │   ├── toLower.js
│   │   ├── toNumber.js
│   │   ├── toPairsIn.js
│   │   ├── toPairs.js
│   │   ├── toPath.js
│   │   ├── toPlainObject.js
│   │   ├── toSafeInteger.js
│   │   ├── toString.js
│   │   ├── toUpper.js
│   │   ├── transform.js
│   │   ├── trimCharsEnd.js
│   │   ├── trimChars.js
│   │   ├── trimCharsStart.js
│   │   ├── trimEnd.js
│   │   ├── trim.js
│   │   ├── trimStart.js
│   │   ├── truncate.js
│   │   ├── unapply.js
│   │   ├── unary.js
│   │   ├── unescape.js
│   │   ├── unionBy.js
│   │   ├── union.js
│   │   ├── unionWith.js
│   │   ├── uniqBy.js
│   │   ├── uniq.js
│   │   ├── uniqueId.js
│   │   ├── uniqWith.js
│   │   ├── unnest.js
│   │   ├── unset.js
│   │   ├── unzip.js
│   │   ├── unzipWith.js
│   │   ├── update.js
│   │   ├── updateWith.js
│   │   ├── upperCase.js
│   │   ├── upperFirst.js
│   │   ├── useWith.js
│   │   ├── _util.js
│   │   ├── util.js
│   │   ├── value.js
│   │   ├── valueOf.js
│   │   ├── valuesIn.js
│   │   ├── values.js
│   │   ├── whereEq.js
│   │   ├── where.js
│   │   ├── without.js
│   │   ├── words.js
│   │   ├── wrap.js
│   │   ├── wrapperAt.js
│   │   ├── wrapperChain.js
│   │   ├── wrapperLodash.js
│   │   ├── wrapperReverse.js
│   │   ├── wrapperValue.js
│   │   ├── xorBy.js
│   │   ├── xor.js
│   │   ├── xorWith.js
│   │   ├── zipAll.js
│   │   ├── zip.js
│   │   ├── zipObjectDeep.js
│   │   ├── zipObject.js
│   │   ├── zipObj.js
│   │   └── zipWith.js
│   ├── fp.js
│   ├── _freeGlobal.js
│   ├── fromPairs.js
│   ├── function.js
│   ├── functionsIn.js
│   ├── functions.js
│   ├── _getAllKeysIn.js
│   ├── _getAllKeys.js
│   ├── _getData.js
│   ├── _getFuncName.js
│   ├── _getHolder.js
│   ├── get.js
│   ├── _getMapData.js
│   ├── _getMatchData.js
│   ├── _getNative.js
│   ├── _getPrototype.js
│   ├── _getRawTag.js
│   ├── _getSymbolsIn.js
│   ├── _getSymbols.js
│   ├── _getTag.js
│   ├── _getValue.js
│   ├── _getView.js
│   ├── _getWrapDetails.js
│   ├── groupBy.js
│   ├── gte.js
│   ├── gt.js
│   ├── _hashClear.js
│   ├── _hashDelete.js
│   ├── _hashGet.js
│   ├── _hashHas.js
│   ├── _Hash.js
│   ├── _hashSet.js
│   ├── hasIn.js
│   ├── has.js
│   ├── _hasPath.js
│   ├── _hasUnicode.js
│   ├── _hasUnicodeWord.js
│   ├── head.js
│   ├── identity.js
│   ├── includes.js
│   ├── index.js
│   ├── indexOf.js
│   ├── _initCloneArray.js
│   ├── _initCloneByTag.js
│   ├── _initCloneObject.js
│   ├── initial.js
│   ├── inRange.js
│   ├── _insertWrapDetails.js
│   ├── intersectionBy.js
│   ├── intersection.js
│   ├── intersectionWith.js
│   ├── invertBy.js
│   ├── invert.js
│   ├── invoke.js
│   ├── invokeMap.js
│   ├── isArguments.js
│   ├── isArrayBuffer.js
│   ├── isArray.js
│   ├── isArrayLike.js
│   ├── isArrayLikeObject.js
│   ├── isBoolean.js
│   ├── isBuffer.js
│   ├── isDate.js
│   ├── isElement.js
│   ├── isEmpty.js
│   ├── isEqual.js
│   ├── isEqualWith.js
│   ├── isError.js
│   ├── isFinite.js
│   ├── _isFlattenable.js
│   ├── isFunction.js
│   ├── _isIndex.js
│   ├── isInteger.js
│   ├── _isIterateeCall.js
│   ├── _isKeyable.js
│   ├── _isKey.js
│   ├── _isLaziable.js
│   ├── isLength.js
│   ├── isMap.js
│   ├── _isMaskable.js
│   ├── _isMasked.js
│   ├── isMatch.js
│   ├── isMatchWith.js
│   ├── isNaN.js
│   ├── isNative.js
│   ├── isNil.js
│   ├── isNull.js
│   ├── isNumber.js
│   ├── isObject.js
│   ├── isObjectLike.js
│   ├── isPlainObject.js
│   ├── _isPrototype.js
│   ├── isRegExp.js
│   ├── isSafeInteger.js
│   ├── isSet.js
│   ├── _isStrictComparable.js
│   ├── isString.js
│   ├── isSymbol.js
│   ├── isTypedArray.js
│   ├── isUndefined.js
│   ├── isWeakMap.js
│   ├── isWeakSet.js
│   ├── iteratee.js
│   ├── _iteratorToArray.js
│   ├── join.js
│   ├── kebabCase.js
│   ├── keyBy.js
│   ├── keysIn.js
│   ├── keys.js
│   ├── lang.js
│   ├── lastIndexOf.js
│   ├── last.js
│   ├── _lazyClone.js
│   ├── _lazyReverse.js
│   ├── _lazyValue.js
│   ├── _LazyWrapper.js
│   ├── LICENSE
│   ├── _listCacheClear.js
│   ├── _listCacheDelete.js
│   ├── _listCacheGet.js
│   ├── _listCacheHas.js
│   ├── _ListCache.js
│   ├── _listCacheSet.js
│   ├── lodash.js
│   ├── lodash.min.js
│   ├── _LodashWrapper.js
│   ├── lowerCase.js
│   ├── lowerFirst.js
│   ├── lte.js
│   ├── lt.js
│   ├── _mapCacheClear.js
│   ├── _mapCacheDelete.js
│   ├── _mapCacheGet.js
│   ├── _mapCacheHas.js
│   ├── _MapCache.js
│   ├── _mapCacheSet.js
│   ├── map.js
│   ├── _Map.js
│   ├── mapKeys.js
│   ├── _mapToArray.js
│   ├── mapValues.js
│   ├── matches.js
│   ├── matchesProperty.js
│   ├── _matchesStrictComparable.js
│   ├── math.js
│   ├── maxBy.js
│   ├── max.js
│   ├── meanBy.js
│   ├── mean.js
│   ├── _memoizeCapped.js
│   ├── memoize.js
│   ├── _mergeData.js
│   ├── merge.js
│   ├── mergeWith.js
│   ├── _metaMap.js
│   ├── method.js
│   ├── methodOf.js
│   ├── minBy.js
│   ├── min.js
│   ├── mixin.js
│   ├── multiply.js
│   ├── _nativeCreate.js
│   ├── _nativeKeysIn.js
│   ├── _nativeKeys.js
│   ├── negate.js
│   ├── next.js
│   ├── _nodeUtil.js
│   ├── noop.js
│   ├── now.js
│   ├── nthArg.js
│   ├── nth.js
│   ├── number.js
│   ├── object.js
│   ├── _objectToString.js
│   ├── omitBy.js
│   ├── omit.js
│   ├── once.js
│   ├── orderBy.js
│   ├── _overArg.js
│   ├── overArgs.js
│   ├── overEvery.js
│   ├── over.js
│   ├── _overRest.js
│   ├── overSome.js
│   ├── package.json
│   ├── padEnd.js
│   ├── pad.js
│   ├── padStart.js
│   ├── _parent.js
│   ├── parseInt.js
│   ├── partial.js
│   ├── partialRight.js
│   ├── partition.js
│   ├── pickBy.js
│   ├── pick.js
│   ├── plant.js
│   ├── _Promise.js
│   ├── property.js
│   ├── propertyOf.js
│   ├── pullAllBy.js
│   ├── pullAll.js
│   ├── pullAllWith.js
│   ├── pullAt.js
│   ├── pull.js
│   ├── random.js
│   ├── range.js
│   ├── rangeRight.js
│   ├── README.md
│   ├── _realNames.js
│   ├── rearg.js
│   ├── reduce.js
│   ├── reduceRight.js
│   ├── _reEscape.js
│   ├── _reEvaluate.js
│   ├── _reInterpolate.js
│   ├── reject.js
│   ├── release.md
│   ├── remove.js
│   ├── _reorder.js
│   ├── repeat.js
│   ├── _replaceHolders.js
│   ├── replace.js
│   ├── rest.js
│   ├── result.js
│   ├── reverse.js
│   ├── _root.js
│   ├── round.js
│   ├── _safeGet.js
│   ├── sample.js
│   ├── sampleSize.js
│   ├── seq.js
│   ├── _setCacheAdd.js
│   ├── _setCacheHas.js
│   ├── _SetCache.js
│   ├── _setData.js
│   ├── set.js
│   ├── _Set.js
│   ├── _setToArray.js
│   ├── _setToPairs.js
│   ├── _setToString.js
│   ├── setWith.js
│   ├── _setWrapToString.js
│   ├── _shortOut.js
│   ├── shuffle.js
│   ├── _shuffleSelf.js
│   ├── size.js
│   ├── slice.js
│   ├── snakeCase.js
│   ├── some.js
│   ├── sortBy.js
│   ├── sortedIndexBy.js
│   ├── sortedIndex.js
│   ├── sortedIndexOf.js
│   ├── sortedLastIndexBy.js
│   ├── sortedLastIndex.js
│   ├── sortedLastIndexOf.js
│   ├── sortedUniqBy.js
│   ├── sortedUniq.js
│   ├── split.js
│   ├── spread.js
│   ├── _stackClear.js
│   ├── _stackDelete.js
│   ├── _stackGet.js
│   ├── _stackHas.js
│   ├── _Stack.js
│   ├── _stackSet.js
│   ├── startCase.js
│   ├── startsWith.js
│   ├── _strictIndexOf.js
│   ├── _strictLastIndexOf.js
│   ├── string.js
│   ├── _stringSize.js
│   ├── _stringToArray.js
│   ├── _stringToPath.js
│   ├── stubArray.js
│   ├── stubFalse.js
│   ├── stubObject.js
│   ├── stubString.js
│   ├── stubTrue.js
│   ├── subtract.js
│   ├── sumBy.js
│   ├── sum.js
│   ├── _Symbol.js
│   ├── tail.js
│   ├── take.js
│   ├── takeRight.js
│   ├── takeRightWhile.js
│   ├── takeWhile.js
│   ├── tap.js
│   ├── template.js
│   ├── templateSettings.js
│   ├── throttle.js
│   ├── thru.js
│   ├── times.js
│   ├── toArray.js
│   ├── toFinite.js
│   ├── toInteger.js
│   ├── toIterator.js
│   ├── toJSON.js
│   ├── _toKey.js
│   ├── toLength.js
│   ├── toLower.js
│   ├── toNumber.js
│   ├── toPairsIn.js
│   ├── toPairs.js
│   ├── toPath.js
│   ├── toPlainObject.js
│   ├── toSafeInteger.js
│   ├── _toSource.js
│   ├── toString.js
│   ├── toUpper.js
│   ├── transform.js
│   ├── trimEnd.js
│   ├── trim.js
│   ├── _trimmedEndIndex.js
│   ├── trimStart.js
│   ├── truncate.js
│   ├── _Uint8Array.js
│   ├── unary.js
│   ├── _unescapeHtmlChar.js
│   ├── unescape.js
│   ├── _unicodeSize.js
│   ├── _unicodeToArray.js
│   ├── _unicodeWords.js
│   ├── unionBy.js
│   ├── union.js
│   ├── unionWith.js
│   ├── uniqBy.js
│   ├── uniq.js
│   ├── uniqueId.js
│   ├── uniqWith.js
│   ├── unset.js
│   ├── unzip.js
│   ├── unzipWith.js
│   ├── update.js
│   ├── updateWith.js
│   ├── _updateWrapDetails.js
│   ├── upperCase.js
│   ├── upperFirst.js
│   ├── util.js
│   ├── value.js
│   ├── valueOf.js
│   ├── valuesIn.js
│   ├── values.js
│   ├── _WeakMap.js
│   ├── without.js
│   ├── words.js
│   ├── wrap.js
│   ├── wrapperAt.js
│   ├── wrapperChain.js
│   ├── _wrapperClone.js
│   ├── wrapperLodash.js
│   ├── wrapperReverse.js
│   ├── wrapperValue.js
│   ├── xorBy.js
│   ├── xor.js
│   ├── xorWith.js
│   ├── zip.js
│   ├── zipObjectDeep.js
│   ├── zipObject.js
│   └── zipWith.js
└── [01;34mpicocolors[0m
    ├── LICENSE
    ├── package.json
    ├── picocolors.browser.js
    ├── picocolors.d.ts
    ├── picocolors.js
    ├── README.md
    └── types.ts

3 directories, 1061 files
```

## ***Instalación de otros paquetes:***

- *Cuando instalamos paquetes adicionales, como `lodash` o `react`, npm creará un directorio con el nombre del paquete dentro del directorio `node_modules`, el cual contendrá varios ficheros y subdirectorios.*

### ***Instalación de React***

**Para instalar `react`, puedes usar el siguiente comando:**

```bash
npm install react
```

### ***Estructura del directorio `node_modules`:***

- *Al instalar `react`, también se instalan automáticamente sus dependencias, lo que resulta en un árbol de directorios aún más grande.*

- *Estos directorios contienen ficheros y subdirectorios necesarios para que las bibliotecas funcionen correctamente. Todas estas son dependencias de nuestras dependencias, lo que significa que, además de los ficheros principales del paquete, también se incluyen los ficheros y módulos que dichos paquetes necesitan para funcionar.*

- *Después de instalar paquetes como `lodash` y `react`, el directorio `node_modules` se veria de la siguiente manera.*

```bash
[01;34m./node_modules/[0m
├── [01;34mjs-tokens[0m
│   ├── CHANGELOG.md
│   ├── index.js
│   ├── LICENSE
│   ├── package.json
│   └── README.md
├── [01;34mlodash[0m
│   ├── add.js
│   ├── after.js
│   ├── _apply.js
│   ├── _arrayAggregator.js
│   ├── _arrayEach.js
│   ├── _arrayEachRight.js
│   ├── _arrayEvery.js
│   ├── _arrayFilter.js
│   ├── _arrayIncludes.js
│   ├── _arrayIncludesWith.js
│   ├── array.js
│   ├── _arrayLikeKeys.js
│   ├── _arrayMap.js
│   ├── _arrayPush.js
│   ├── _arrayReduce.js
│   ├── _arrayReduceRight.js
│   ├── _arraySample.js
│   ├── _arraySampleSize.js
│   ├── _arrayShuffle.js
│   ├── _arraySome.js
│   ├── ary.js
│   ├── _asciiSize.js
│   ├── _asciiToArray.js
│   ├── _asciiWords.js
│   ├── assignIn.js
│   ├── assignInWith.js
│   ├── assign.js
│   ├── _assignMergeValue.js
│   ├── _assignValue.js
│   ├── assignWith.js
│   ├── _assocIndexOf.js
│   ├── at.js
│   ├── attempt.js
│   ├── _baseAggregator.js
│   ├── _baseAssignIn.js
│   ├── _baseAssign.js
│   ├── _baseAssignValue.js
│   ├── _baseAt.js
│   ├── _baseClamp.js
│   ├── _baseClone.js
│   ├── _baseConforms.js
│   ├── _baseConformsTo.js
│   ├── _baseCreate.js
│   ├── _baseDelay.js
│   ├── _baseDifference.js
│   ├── _baseEach.js
│   ├── _baseEachRight.js
│   ├── _baseEvery.js
│   ├── _baseExtremum.js
│   ├── _baseFill.js
│   ├── _baseFilter.js
│   ├── _baseFindIndex.js
│   ├── _baseFindKey.js
│   ├── _baseFlatten.js
│   ├── _baseFor.js
│   ├── _baseForOwn.js
│   ├── _baseForOwnRight.js
│   ├── _baseForRight.js
│   ├── _baseFunctions.js
│   ├── _baseGetAllKeys.js
│   ├── _baseGet.js
│   ├── _baseGetTag.js
│   ├── _baseGt.js
│   ├── _baseHasIn.js
│   ├── _baseHas.js
│   ├── _baseIndexOf.js
│   ├── _baseIndexOfWith.js
│   ├── _baseInRange.js
│   ├── _baseIntersection.js
│   ├── _baseInverter.js
│   ├── _baseInvoke.js
│   ├── _baseIsArguments.js
│   ├── _baseIsArrayBuffer.js
│   ├── _baseIsDate.js
│   ├── _baseIsEqualDeep.js
│   ├── _baseIsEqual.js
│   ├── _baseIsMap.js
│   ├── _baseIsMatch.js
│   ├── _baseIsNaN.js
│   ├── _baseIsNative.js
│   ├── _baseIsRegExp.js
│   ├── _baseIsSet.js
│   ├── _baseIsTypedArray.js
│   ├── _baseIteratee.js
│   ├── _baseKeysIn.js
│   ├── _baseKeys.js
│   ├── _baseLodash.js
│   ├── _baseLt.js
│   ├── _baseMap.js
│   ├── _baseMatches.js
│   ├── _baseMatchesProperty.js
│   ├── _baseMean.js
│   ├── _baseMergeDeep.js
│   ├── _baseMerge.js
│   ├── _baseNth.js
│   ├── _baseOrderBy.js
│   ├── _basePickBy.js
│   ├── _basePick.js
│   ├── _basePropertyDeep.js
│   ├── _baseProperty.js
│   ├── _basePropertyOf.js
│   ├── _basePullAll.js
│   ├── _basePullAt.js
│   ├── _baseRandom.js
│   ├── _baseRange.js
│   ├── _baseReduce.js
│   ├── _baseRepeat.js
│   ├── _baseRest.js
│   ├── _baseSample.js
│   ├── _baseSampleSize.js
│   ├── _baseSetData.js
│   ├── _baseSet.js
│   ├── _baseSetToString.js
│   ├── _baseShuffle.js
│   ├── _baseSlice.js
│   ├── _baseSome.js
│   ├── _baseSortBy.js
│   ├── _baseSortedIndexBy.js
│   ├── _baseSortedIndex.js
│   ├── _baseSortedUniq.js
│   ├── _baseSum.js
│   ├── _baseTimes.js
│   ├── _baseToNumber.js
│   ├── _baseToPairs.js
│   ├── _baseToString.js
│   ├── _baseTrim.js
│   ├── _baseUnary.js
│   ├── _baseUniq.js
│   ├── _baseUnset.js
│   ├── _baseUpdate.js
│   ├── _baseValues.js
│   ├── _baseWhile.js
│   ├── _baseWrapperValue.js
│   ├── _baseXor.js
│   ├── _baseZipObject.js
│   ├── before.js
│   ├── bindAll.js
│   ├── bind.js
│   ├── bindKey.js
│   ├── _cacheHas.js
│   ├── camelCase.js
│   ├── capitalize.js
│   ├── castArray.js
│   ├── _castArrayLikeObject.js
│   ├── _castFunction.js
│   ├── _castPath.js
│   ├── _castRest.js
│   ├── _castSlice.js
│   ├── ceil.js
│   ├── chain.js
│   ├── _charsEndIndex.js
│   ├── _charsStartIndex.js
│   ├── chunk.js
│   ├── clamp.js
│   ├── _cloneArrayBuffer.js
│   ├── _cloneBuffer.js
│   ├── _cloneDataView.js
│   ├── cloneDeep.js
│   ├── cloneDeepWith.js
│   ├── clone.js
│   ├── _cloneRegExp.js
│   ├── _cloneSymbol.js
│   ├── _cloneTypedArray.js
│   ├── cloneWith.js
│   ├── collection.js
│   ├── commit.js
│   ├── compact.js
│   ├── _compareAscending.js
│   ├── _compareMultiple.js
│   ├── _composeArgs.js
│   ├── _composeArgsRight.js
│   ├── concat.js
│   ├── cond.js
│   ├── conforms.js
│   ├── conformsTo.js
│   ├── constant.js
│   ├── _copyArray.js
│   ├── _copyObject.js
│   ├── _copySymbolsIn.js
│   ├── _copySymbols.js
│   ├── core.js
│   ├── _coreJsData.js
│   ├── core.min.js
│   ├── countBy.js
│   ├── _countHolders.js
│   ├── _createAggregator.js
│   ├── _createAssigner.js
│   ├── _createBaseEach.js
│   ├── _createBaseFor.js
│   ├── _createBind.js
│   ├── _createCaseFirst.js
│   ├── _createCompounder.js
│   ├── _createCtor.js
│   ├── _createCurry.js
│   ├── _createFind.js
│   ├── _createFlow.js
│   ├── _createHybrid.js
│   ├── _createInverter.js
│   ├── create.js
│   ├── _createMathOperation.js
│   ├── _createOver.js
│   ├── _createPadding.js
│   ├── _createPartial.js
│   ├── _createRange.js
│   ├── _createRecurry.js
│   ├── _createRelationalOperation.js
│   ├── _createRound.js
│   ├── _createSet.js
│   ├── _createToPairs.js
│   ├── _createWrap.js
│   ├── curry.js
│   ├── curryRight.js
│   ├── _customDefaultsAssignIn.js
│   ├── _customDefaultsMerge.js
│   ├── _customOmitClone.js
│   ├── _DataView.js
│   ├── date.js
│   ├── debounce.js
│   ├── deburr.js
│   ├── _deburrLetter.js
│   ├── defaultsDeep.js
│   ├── defaults.js
│   ├── defaultTo.js
│   ├── defer.js
│   ├── _defineProperty.js
│   ├── delay.js
│   ├── differenceBy.js
│   ├── difference.js
│   ├── differenceWith.js
│   ├── divide.js
│   ├── drop.js
│   ├── dropRight.js
│   ├── dropRightWhile.js
│   ├── dropWhile.js
│   ├── each.js
│   ├── eachRight.js
│   ├── endsWith.js
│   ├── entriesIn.js
│   ├── entries.js
│   ├── eq.js
│   ├── _equalArrays.js
│   ├── _equalByTag.js
│   ├── _equalObjects.js
│   ├── _escapeHtmlChar.js
│   ├── escape.js
│   ├── escapeRegExp.js
│   ├── _escapeStringChar.js
│   ├── every.js
│   ├── extend.js
│   ├── extendWith.js
│   ├── fill.js
│   ├── filter.js
│   ├── findIndex.js
│   ├── find.js
│   ├── findKey.js
│   ├── findLastIndex.js
│   ├── findLast.js
│   ├── findLastKey.js
│   ├── first.js
│   ├── flake.lock
│   ├── flake.nix
│   ├── flatMapDeep.js
│   ├── flatMapDepth.js
│   ├── flatMap.js
│   ├── _flatRest.js
│   ├── flattenDeep.js
│   ├── flattenDepth.js
│   ├── flatten.js
│   ├── flip.js
│   ├── floor.js
│   ├── flow.js
│   ├── flowRight.js
│   ├── forEach.js
│   ├── forEachRight.js
│   ├── forIn.js
│   ├── forInRight.js
│   ├── forOwn.js
│   ├── forOwnRight.js
│   ├── [01;34mfp[0m
│   │   ├── add.js
│   │   ├── after.js
│   │   ├── all.js
│   │   ├── allPass.js
│   │   ├── always.js
│   │   ├── any.js
│   │   ├── anyPass.js
│   │   ├── apply.js
│   │   ├── array.js
│   │   ├── ary.js
│   │   ├── assignAll.js
│   │   ├── assignAllWith.js
│   │   ├── assignInAll.js
│   │   ├── assignInAllWith.js
│   │   ├── assignIn.js
│   │   ├── assignInWith.js
│   │   ├── assign.js
│   │   ├── assignWith.js
│   │   ├── assoc.js
│   │   ├── assocPath.js
│   │   ├── at.js
│   │   ├── attempt.js
│   │   ├── _baseConvert.js
│   │   ├── before.js
│   │   ├── bindAll.js
│   │   ├── bind.js
│   │   ├── bindKey.js
│   │   ├── camelCase.js
│   │   ├── capitalize.js
│   │   ├── castArray.js
│   │   ├── ceil.js
│   │   ├── chain.js
│   │   ├── chunk.js
│   │   ├── clamp.js
│   │   ├── cloneDeep.js
│   │   ├── cloneDeepWith.js
│   │   ├── clone.js
│   │   ├── cloneWith.js
│   │   ├── collection.js
│   │   ├── commit.js
│   │   ├── compact.js
│   │   ├── complement.js
│   │   ├── compose.js
│   │   ├── concat.js
│   │   ├── cond.js
│   │   ├── conforms.js
│   │   ├── conformsTo.js
│   │   ├── constant.js
│   │   ├── contains.js
│   │   ├── _convertBrowser.js
│   │   ├── convert.js
│   │   ├── countBy.js
│   │   ├── create.js
│   │   ├── curry.js
│   │   ├── curryN.js
│   │   ├── curryRight.js
│   │   ├── curryRightN.js
│   │   ├── date.js
│   │   ├── debounce.js
│   │   ├── deburr.js
│   │   ├── defaultsAll.js
│   │   ├── defaultsDeepAll.js
│   │   ├── defaultsDeep.js
│   │   ├── defaults.js
│   │   ├── defaultTo.js
│   │   ├── defer.js
│   │   ├── delay.js
│   │   ├── differenceBy.js
│   │   ├── difference.js
│   │   ├── differenceWith.js
│   │   ├── dissoc.js
│   │   ├── dissocPath.js
│   │   ├── divide.js
│   │   ├── drop.js
│   │   ├── dropLast.js
│   │   ├── dropLastWhile.js
│   │   ├── dropRight.js
│   │   ├── dropRightWhile.js
│   │   ├── dropWhile.js
│   │   ├── each.js
│   │   ├── eachRight.js
│   │   ├── endsWith.js
│   │   ├── entriesIn.js
│   │   ├── entries.js
│   │   ├── eq.js
│   │   ├── equals.js
│   │   ├── escape.js
│   │   ├── escapeRegExp.js
│   │   ├── every.js
│   │   ├── extendAll.js
│   │   ├── extendAllWith.js
│   │   ├── extend.js
│   │   ├── extendWith.js
│   │   ├── _falseOptions.js
│   │   ├── fill.js
│   │   ├── filter.js
│   │   ├── findFrom.js
│   │   ├── findIndexFrom.js
│   │   ├── findIndex.js
│   │   ├── find.js
│   │   ├── findKey.js
│   │   ├── findLastFrom.js
│   │   ├── findLastIndexFrom.js
│   │   ├── findLastIndex.js
│   │   ├── findLast.js
│   │   ├── findLastKey.js
│   │   ├── first.js
│   │   ├── F.js
│   │   ├── flatMapDeep.js
│   │   ├── flatMapDepth.js
│   │   ├── flatMap.js
│   │   ├── flattenDeep.js
│   │   ├── flattenDepth.js
│   │   ├── flatten.js
│   │   ├── flip.js
│   │   ├── floor.js
│   │   ├── flow.js
│   │   ├── flowRight.js
│   │   ├── forEach.js
│   │   ├── forEachRight.js
│   │   ├── forIn.js
│   │   ├── forInRight.js
│   │   ├── forOwn.js
│   │   ├── forOwnRight.js
│   │   ├── fromPairs.js
│   │   ├── function.js
│   │   ├── functionsIn.js
│   │   ├── functions.js
│   │   ├── get.js
│   │   ├── getOr.js
│   │   ├── groupBy.js
│   │   ├── gte.js
│   │   ├── gt.js
│   │   ├── hasIn.js
│   │   ├── has.js
│   │   ├── head.js
│   │   ├── identical.js
│   │   ├── identity.js
│   │   ├── includesFrom.js
│   │   ├── includes.js
│   │   ├── indexBy.js
│   │   ├── indexOfFrom.js
│   │   ├── indexOf.js
│   │   ├── initial.js
│   │   ├── init.js
│   │   ├── inRange.js
│   │   ├── intersectionBy.js
│   │   ├── intersection.js
│   │   ├── intersectionWith.js
│   │   ├── invertBy.js
│   │   ├── invert.js
│   │   ├── invertObj.js
│   │   ├── invokeArgs.js
│   │   ├── invokeArgsMap.js
│   │   ├── invoke.js
│   │   ├── invokeMap.js
│   │   ├── isArguments.js
│   │   ├── isArrayBuffer.js
│   │   ├── isArray.js
│   │   ├── isArrayLike.js
│   │   ├── isArrayLikeObject.js
│   │   ├── isBoolean.js
│   │   ├── isBuffer.js
│   │   ├── isDate.js
│   │   ├── isElement.js
│   │   ├── isEmpty.js
│   │   ├── isEqual.js
│   │   ├── isEqualWith.js
│   │   ├── isError.js
│   │   ├── isFinite.js
│   │   ├── isFunction.js
│   │   ├── isInteger.js
│   │   ├── isLength.js
│   │   ├── isMap.js
│   │   ├── isMatch.js
│   │   ├── isMatchWith.js
│   │   ├── isNaN.js
│   │   ├── isNative.js
│   │   ├── isNil.js
│   │   ├── isNull.js
│   │   ├── isNumber.js
│   │   ├── isObject.js
│   │   ├── isObjectLike.js
│   │   ├── isPlainObject.js
│   │   ├── isRegExp.js
│   │   ├── isSafeInteger.js
│   │   ├── isSet.js
│   │   ├── isString.js
│   │   ├── isSymbol.js
│   │   ├── isTypedArray.js
│   │   ├── isUndefined.js
│   │   ├── isWeakMap.js
│   │   ├── isWeakSet.js
│   │   ├── iteratee.js
│   │   ├── join.js
│   │   ├── __.js
│   │   ├── juxt.js
│   │   ├── kebabCase.js
│   │   ├── keyBy.js
│   │   ├── keysIn.js
│   │   ├── keys.js
│   │   ├── lang.js
│   │   ├── lastIndexOfFrom.js
│   │   ├── lastIndexOf.js
│   │   ├── last.js
│   │   ├── lowerCase.js
│   │   ├── lowerFirst.js
│   │   ├── lte.js
│   │   ├── lt.js
│   │   ├── map.js
│   │   ├── mapKeys.js
│   │   ├── _mapping.js
│   │   ├── mapValues.js
│   │   ├── matches.js
│   │   ├── matchesProperty.js
│   │   ├── math.js
│   │   ├── maxBy.js
│   │   ├── max.js
│   │   ├── meanBy.js
│   │   ├── mean.js
│   │   ├── memoize.js
│   │   ├── mergeAll.js
│   │   ├── mergeAllWith.js
│   │   ├── merge.js
│   │   ├── mergeWith.js
│   │   ├── method.js
│   │   ├── methodOf.js
│   │   ├── minBy.js
│   │   ├── min.js
│   │   ├── mixin.js
│   │   ├── multiply.js
│   │   ├── nAry.js
│   │   ├── negate.js
│   │   ├── next.js
│   │   ├── noop.js
│   │   ├── now.js
│   │   ├── nthArg.js
│   │   ├── nth.js
│   │   ├── number.js
│   │   ├── object.js
│   │   ├── omitAll.js
│   │   ├── omitBy.js
│   │   ├── omit.js
│   │   ├── once.js
│   │   ├── orderBy.js
│   │   ├── overArgs.js
│   │   ├── overEvery.js
│   │   ├── over.js
│   │   ├── overSome.js
│   │   ├── padCharsEnd.js
│   │   ├── padChars.js
│   │   ├── padCharsStart.js
│   │   ├── padEnd.js
│   │   ├── pad.js
│   │   ├── padStart.js
│   │   ├── parseInt.js
│   │   ├── partial.js
│   │   ├── partialRight.js
│   │   ├── partition.js
│   │   ├── pathEq.js
│   │   ├── path.js
│   │   ├── pathOr.js
│   │   ├── paths.js
│   │   ├── pickAll.js
│   │   ├── pickBy.js
│   │   ├── pick.js
│   │   ├── pipe.js
│   │   ├── placeholder.js
│   │   ├── plant.js
│   │   ├── pluck.js
│   │   ├── propEq.js
│   │   ├── property.js
│   │   ├── propertyOf.js
│   │   ├── prop.js
│   │   ├── propOr.js
│   │   ├── props.js
│   │   ├── pullAllBy.js
│   │   ├── pullAll.js
│   │   ├── pullAllWith.js
│   │   ├── pullAt.js
│   │   ├── pull.js
│   │   ├── random.js
│   │   ├── range.js
│   │   ├── rangeRight.js
│   │   ├── rangeStep.js
│   │   ├── rangeStepRight.js
│   │   ├── rearg.js
│   │   ├── reduce.js
│   │   ├── reduceRight.js
│   │   ├── reject.js
│   │   ├── remove.js
│   │   ├── repeat.js
│   │   ├── replace.js
│   │   ├── restFrom.js
│   │   ├── rest.js
│   │   ├── result.js
│   │   ├── reverse.js
│   │   ├── round.js
│   │   ├── sample.js
│   │   ├── sampleSize.js
│   │   ├── seq.js
│   │   ├── set.js
│   │   ├── setWith.js
│   │   ├── shuffle.js
│   │   ├── size.js
│   │   ├── slice.js
│   │   ├── snakeCase.js
│   │   ├── some.js
│   │   ├── sortBy.js
│   │   ├── sortedIndexBy.js
│   │   ├── sortedIndex.js
│   │   ├── sortedIndexOf.js
│   │   ├── sortedLastIndexBy.js
│   │   ├── sortedLastIndex.js
│   │   ├── sortedLastIndexOf.js
│   │   ├── sortedUniqBy.js
│   │   ├── sortedUniq.js
│   │   ├── split.js
│   │   ├── spreadFrom.js
│   │   ├── spread.js
│   │   ├── startCase.js
│   │   ├── startsWith.js
│   │   ├── string.js
│   │   ├── stubArray.js
│   │   ├── stubFalse.js
│   │   ├── stubObject.js
│   │   ├── stubString.js
│   │   ├── stubTrue.js
│   │   ├── subtract.js
│   │   ├── sumBy.js
│   │   ├── sum.js
│   │   ├── symmetricDifferenceBy.js
│   │   ├── symmetricDifference.js
│   │   ├── symmetricDifferenceWith.js
│   │   ├── tail.js
│   │   ├── take.js
│   │   ├── takeLast.js
│   │   ├── takeLastWhile.js
│   │   ├── takeRight.js
│   │   ├── takeRightWhile.js
│   │   ├── takeWhile.js
│   │   ├── tap.js
│   │   ├── template.js
│   │   ├── templateSettings.js
│   │   ├── throttle.js
│   │   ├── thru.js
│   │   ├── times.js
│   │   ├── T.js
│   │   ├── toArray.js
│   │   ├── toFinite.js
│   │   ├── toInteger.js
│   │   ├── toIterator.js
│   │   ├── toJSON.js
│   │   ├── toLength.js
│   │   ├── toLower.js
│   │   ├── toNumber.js
│   │   ├── toPairsIn.js
│   │   ├── toPairs.js
│   │   ├── toPath.js
│   │   ├── toPlainObject.js
│   │   ├── toSafeInteger.js
│   │   ├── toString.js
│   │   ├── toUpper.js
│   │   ├── transform.js
│   │   ├── trimCharsEnd.js
│   │   ├── trimChars.js
│   │   ├── trimCharsStart.js
│   │   ├── trimEnd.js
│   │   ├── trim.js
│   │   ├── trimStart.js
│   │   ├── truncate.js
│   │   ├── unapply.js
│   │   ├── unary.js
│   │   ├── unescape.js
│   │   ├── unionBy.js
│   │   ├── union.js
│   │   ├── unionWith.js
│   │   ├── uniqBy.js
│   │   ├── uniq.js
│   │   ├── uniqueId.js
│   │   ├── uniqWith.js
│   │   ├── unnest.js
│   │   ├── unset.js
│   │   ├── unzip.js
│   │   ├── unzipWith.js
│   │   ├── update.js
│   │   ├── updateWith.js
│   │   ├── upperCase.js
│   │   ├── upperFirst.js
│   │   ├── useWith.js
│   │   ├── _util.js
│   │   ├── util.js
│   │   ├── value.js
│   │   ├── valueOf.js
│   │   ├── valuesIn.js
│   │   ├── values.js
│   │   ├── whereEq.js
│   │   ├── where.js
│   │   ├── without.js
│   │   ├── words.js
│   │   ├── wrap.js
│   │   ├── wrapperAt.js
│   │   ├── wrapperChain.js
│   │   ├── wrapperLodash.js
│   │   ├── wrapperReverse.js
│   │   ├── wrapperValue.js
│   │   ├── xorBy.js
│   │   ├── xor.js
│   │   ├── xorWith.js
│   │   ├── zipAll.js
│   │   ├── zip.js
│   │   ├── zipObjectDeep.js
│   │   ├── zipObject.js
│   │   ├── zipObj.js
│   │   └── zipWith.js
│   ├── fp.js
│   ├── _freeGlobal.js
│   ├── fromPairs.js
│   ├── function.js
│   ├── functionsIn.js
│   ├── functions.js
│   ├── _getAllKeysIn.js
│   ├── _getAllKeys.js
│   ├── _getData.js
│   ├── _getFuncName.js
│   ├── _getHolder.js
│   ├── get.js
│   ├── _getMapData.js
│   ├── _getMatchData.js
│   ├── _getNative.js
│   ├── _getPrototype.js
│   ├── _getRawTag.js
│   ├── _getSymbolsIn.js
│   ├── _getSymbols.js
│   ├── _getTag.js
│   ├── _getValue.js
│   ├── _getView.js
│   ├── _getWrapDetails.js
│   ├── groupBy.js
│   ├── gte.js
│   ├── gt.js
│   ├── _hashClear.js
│   ├── _hashDelete.js
│   ├── _hashGet.js
│   ├── _hashHas.js
│   ├── _Hash.js
│   ├── _hashSet.js
│   ├── hasIn.js
│   ├── has.js
│   ├── _hasPath.js
│   ├── _hasUnicode.js
│   ├── _hasUnicodeWord.js
│   ├── head.js
│   ├── identity.js
│   ├── includes.js
│   ├── index.js
│   ├── indexOf.js
│   ├── _initCloneArray.js
│   ├── _initCloneByTag.js
│   ├── _initCloneObject.js
│   ├── initial.js
│   ├── inRange.js
│   ├── _insertWrapDetails.js
│   ├── intersectionBy.js
│   ├── intersection.js
│   ├── intersectionWith.js
│   ├── invertBy.js
│   ├── invert.js
│   ├── invoke.js
│   ├── invokeMap.js
│   ├── isArguments.js
│   ├── isArrayBuffer.js
│   ├── isArray.js
│   ├── isArrayLike.js
│   ├── isArrayLikeObject.js
│   ├── isBoolean.js
│   ├── isBuffer.js
│   ├── isDate.js
│   ├── isElement.js
│   ├── isEmpty.js
│   ├── isEqual.js
│   ├── isEqualWith.js
│   ├── isError.js
│   ├── isFinite.js
│   ├── _isFlattenable.js
│   ├── isFunction.js
│   ├── _isIndex.js
│   ├── isInteger.js
│   ├── _isIterateeCall.js
│   ├── _isKeyable.js
│   ├── _isKey.js
│   ├── _isLaziable.js
│   ├── isLength.js
│   ├── isMap.js
│   ├── _isMaskable.js
│   ├── _isMasked.js
│   ├── isMatch.js
│   ├── isMatchWith.js
│   ├── isNaN.js
│   ├── isNative.js
│   ├── isNil.js
│   ├── isNull.js
│   ├── isNumber.js
│   ├── isObject.js
│   ├── isObjectLike.js
│   ├── isPlainObject.js
│   ├── _isPrototype.js
│   ├── isRegExp.js
│   ├── isSafeInteger.js
│   ├── isSet.js
│   ├── _isStrictComparable.js
│   ├── isString.js
│   ├── isSymbol.js
│   ├── isTypedArray.js
│   ├── isUndefined.js
│   ├── isWeakMap.js
│   ├── isWeakSet.js
│   ├── iteratee.js
│   ├── _iteratorToArray.js
│   ├── join.js
│   ├── kebabCase.js
│   ├── keyBy.js
│   ├── keysIn.js
│   ├── keys.js
│   ├── lang.js
│   ├── lastIndexOf.js
│   ├── last.js
│   ├── _lazyClone.js
│   ├── _lazyReverse.js
│   ├── _lazyValue.js
│   ├── _LazyWrapper.js
│   ├── LICENSE
│   ├── _listCacheClear.js
│   ├── _listCacheDelete.js
│   ├── _listCacheGet.js
│   ├── _listCacheHas.js
│   ├── _ListCache.js
│   ├── _listCacheSet.js
│   ├── lodash.js
│   ├── lodash.min.js
│   ├── _LodashWrapper.js
│   ├── lowerCase.js
│   ├── lowerFirst.js
│   ├── lte.js
│   ├── lt.js
│   ├── _mapCacheClear.js
│   ├── _mapCacheDelete.js
│   ├── _mapCacheGet.js
│   ├── _mapCacheHas.js
│   ├── _MapCache.js
│   ├── _mapCacheSet.js
│   ├── map.js
│   ├── _Map.js
│   ├── mapKeys.js
│   ├── _mapToArray.js
│   ├── mapValues.js
│   ├── matches.js
│   ├── matchesProperty.js
│   ├── _matchesStrictComparable.js
│   ├── math.js
│   ├── maxBy.js
│   ├── max.js
│   ├── meanBy.js
│   ├── mean.js
│   ├── _memoizeCapped.js
│   ├── memoize.js
│   ├── _mergeData.js
│   ├── merge.js
│   ├── mergeWith.js
│   ├── _metaMap.js
│   ├── method.js
│   ├── methodOf.js
│   ├── minBy.js
│   ├── min.js
│   ├── mixin.js
│   ├── multiply.js
│   ├── _nativeCreate.js
│   ├── _nativeKeysIn.js
│   ├── _nativeKeys.js
│   ├── negate.js
│   ├── next.js
│   ├── _nodeUtil.js
│   ├── noop.js
│   ├── now.js
│   ├── nthArg.js
│   ├── nth.js
│   ├── number.js
│   ├── object.js
│   ├── _objectToString.js
│   ├── omitBy.js
│   ├── omit.js
│   ├── once.js
│   ├── orderBy.js
│   ├── _overArg.js
│   ├── overArgs.js
│   ├── overEvery.js
│   ├── over.js
│   ├── _overRest.js
│   ├── overSome.js
│   ├── package.json
│   ├── padEnd.js
│   ├── pad.js
│   ├── padStart.js
│   ├── _parent.js
│   ├── parseInt.js
│   ├── partial.js
│   ├── partialRight.js
│   ├── partition.js
│   ├── pickBy.js
│   ├── pick.js
│   ├── plant.js
│   ├── _Promise.js
│   ├── property.js
│   ├── propertyOf.js
│   ├── pullAllBy.js
│   ├── pullAll.js
│   ├── pullAllWith.js
│   ├── pullAt.js
│   ├── pull.js
│   ├── random.js
│   ├── range.js
│   ├── rangeRight.js
│   ├── README.md
│   ├── _realNames.js
│   ├── rearg.js
│   ├── reduce.js
│   ├── reduceRight.js
│   ├── _reEscape.js
│   ├── _reEvaluate.js
│   ├── _reInterpolate.js
│   ├── reject.js
│   ├── release.md
│   ├── remove.js
│   ├── _reorder.js
│   ├── repeat.js
│   ├── _replaceHolders.js
│   ├── replace.js
│   ├── rest.js
│   ├── result.js
│   ├── reverse.js
│   ├── _root.js
│   ├── round.js
│   ├── _safeGet.js
│   ├── sample.js
│   ├── sampleSize.js
│   ├── seq.js
│   ├── _setCacheAdd.js
│   ├── _setCacheHas.js
│   ├── _SetCache.js
│   ├── _setData.js
│   ├── set.js
│   ├── _Set.js
│   ├── _setToArray.js
│   ├── _setToPairs.js
│   ├── _setToString.js
│   ├── setWith.js
│   ├── _setWrapToString.js
│   ├── _shortOut.js
│   ├── shuffle.js
│   ├── _shuffleSelf.js
│   ├── size.js
│   ├── slice.js
│   ├── snakeCase.js
│   ├── some.js
│   ├── sortBy.js
│   ├── sortedIndexBy.js
│   ├── sortedIndex.js
│   ├── sortedIndexOf.js
│   ├── sortedLastIndexBy.js
│   ├── sortedLastIndex.js
│   ├── sortedLastIndexOf.js
│   ├── sortedUniqBy.js
│   ├── sortedUniq.js
│   ├── split.js
│   ├── spread.js
│   ├── _stackClear.js
│   ├── _stackDelete.js
│   ├── _stackGet.js
│   ├── _stackHas.js
│   ├── _Stack.js
│   ├── _stackSet.js
│   ├── startCase.js
│   ├── startsWith.js
│   ├── _strictIndexOf.js
│   ├── _strictLastIndexOf.js
│   ├── string.js
│   ├── _stringSize.js
│   ├── _stringToArray.js
│   ├── _stringToPath.js
│   ├── stubArray.js
│   ├── stubFalse.js
│   ├── stubObject.js
│   ├── stubString.js
│   ├── stubTrue.js
│   ├── subtract.js
│   ├── sumBy.js
│   ├── sum.js
│   ├── _Symbol.js
│   ├── tail.js
│   ├── take.js
│   ├── takeRight.js
│   ├── takeRightWhile.js
│   ├── takeWhile.js
│   ├── tap.js
│   ├── template.js
│   ├── templateSettings.js
│   ├── throttle.js
│   ├── thru.js
│   ├── times.js
│   ├── toArray.js
│   ├── toFinite.js
│   ├── toInteger.js
│   ├── toIterator.js
│   ├── toJSON.js
│   ├── _toKey.js
│   ├── toLength.js
│   ├── toLower.js
│   ├── toNumber.js
│   ├── toPairsIn.js
│   ├── toPairs.js
│   ├── toPath.js
│   ├── toPlainObject.js
│   ├── toSafeInteger.js
│   ├── _toSource.js
│   ├── toString.js
│   ├── toUpper.js
│   ├── transform.js
│   ├── trimEnd.js
│   ├── trim.js
│   ├── _trimmedEndIndex.js
│   ├── trimStart.js
│   ├── truncate.js
│   ├── _Uint8Array.js
│   ├── unary.js
│   ├── _unescapeHtmlChar.js
│   ├── unescape.js
│   ├── _unicodeSize.js
│   ├── _unicodeToArray.js
│   ├── _unicodeWords.js
│   ├── unionBy.js
│   ├── union.js
│   ├── unionWith.js
│   ├── uniqBy.js
│   ├── uniq.js
│   ├── uniqueId.js
│   ├── uniqWith.js
│   ├── unset.js
│   ├── unzip.js
│   ├── unzipWith.js
│   ├── update.js
│   ├── updateWith.js
│   ├── _updateWrapDetails.js
│   ├── upperCase.js
│   ├── upperFirst.js
│   ├── util.js
│   ├── value.js
│   ├── valueOf.js
│   ├── valuesIn.js
│   ├── values.js
│   ├── _WeakMap.js
│   ├── without.js
│   ├── words.js
│   ├── wrap.js
│   ├── wrapperAt.js
│   ├── wrapperChain.js
│   ├── _wrapperClone.js
│   ├── wrapperLodash.js
│   ├── wrapperReverse.js
│   ├── wrapperValue.js
│   ├── xorBy.js
│   ├── xor.js
│   ├── xorWith.js
│   ├── zip.js
│   ├── zipObjectDeep.js
│   ├── zipObject.js
│   └── zipWith.js
├── [01;34mloose-envify[0m
│   ├── [01;32mcli.js[0m
│   ├── custom.js
│   ├── index.js
│   ├── LICENSE
│   ├── loose-envify.js
│   ├── package.json
│   ├── README.md
│   └── replace.js
├── [01;34mpicocolors[0m
│   ├── LICENSE
│   ├── package.json
│   ├── picocolors.browser.js
│   ├── picocolors.d.ts
│   ├── picocolors.js
│   ├── README.md
│   └── types.ts
└── [01;34mreact[0m
    ├── [01;34mcjs[0m
    │   ├── react.development.js
    │   ├── react-jsx-dev-runtime.development.js
    │   ├── react-jsx-dev-runtime.production.min.js
    │   ├── react-jsx-dev-runtime.profiling.min.js
    │   ├── react-jsx-runtime.development.js
    │   ├── react-jsx-runtime.production.min.js
    │   ├── react-jsx-runtime.profiling.min.js
    │   ├── react.production.min.js
    │   ├── react.shared-subset.development.js
    │   └── react.shared-subset.production.min.js
    ├── index.js
    ├── jsx-dev-runtime.js
    ├── jsx-runtime.js
    ├── LICENSE
    ├── package.json
    ├── react.shared-subset.js
    ├── README.md
    └── [01;34mumd[0m
        ├── react.development.js
        ├── react.production.min.js
        └── react.profiling.min.js

8 directories, 1094 files
```

**Claro, aquí tienes una versión mejorada y corregida del texto:**

## ***Desinstalación de paquetes***

**Para desinstalar paquetes, como `lodash` y `react`, puedes usar el siguiente comando:**

```bash
npm uninstall lodash react
```

**Esto eliminará las dependencias y actualizará el fichero `package.json`:**

```bash
removed 4 packages, and audited 2 packages in 1s

found 0 vulnerabilities
```

### ***Dependencias de producción y desarrollo***

- *Las dependencias de producción son aquellas que tu aplicación necesita para funcionar. Además, existen dependencias de desarrollo que son necesarias solo durante el desarrollo.*

### ***Instalación de dependencias de desarrollo***

- *Para instalar una dependencia de desarrollo, como [StandardJS](https://standardjs.com/ "https://standardjs.com/"), puedes usar el siguiente comando:*

```bash
npm install standard -D
```

**O alternativamente:**

```bash
npm install standard --save-dev
```

**A continuación se muestra un ejemplo de la instalación de `standard`:**

```bash
npm install standard -D
npm warn deprecated inflight@1.0.6: This module is not supported, and leaks memory. Do not use it. Check out lru-cache if you want a good and tested way to coalesce async requests by a key value, which is much more comprehensive and powerful.
npm warn deprecated @humanwhocodes/config-array@0.11.14: Use @eslint/config-array instead
npm warn deprecated rimraf@3.0.2: Rimraf versions prior to v4 are no longer supported
npm warn deprecated glob@7.2.3: Glob versions prior to v9 are no longer supported
npm warn deprecated @humanwhocodes/object-schema@2.0.3: Use @eslint/object-schema instead

added 249 packages, and audited 251 packages in 7s

111 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
```

### ***Configuración en `package.json`***

**Después de instalar `standard`, el fichero `package.json` se verá así:**

```json
{
  "name": "nodejs",
  "version": "1.0.0",
  "description": "Guía Node.js",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "repository": {
    "type": "git",
    "url": "git+ssh://git@github.com/D4nitrix13/Node-JS.git"
  },
  "keywords": [
    "nodejs",
    "node"
  ],
  "author": "Daniel Benjamin Perez Morales - D4nitrix13",
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/D4nitrix13/Node-JS/issues"
  },
  "homepage": "https://github.com/D4nitrix13/Node-JS#readme",
  "dependencies": {
    "picocolors": "1.0.1"
  },
  "devDependencies": {
    "standard": "17.1.0"
  }
}
```

### ***Uso de ESLint***

- *La dependencia `standard` te ayudará a detectar errores de sintaxis en los ficheros. Para que se resuelvan automáticamente, necesitas una extensión llamada ESLint.*

```bash
Nombre: ESLint
ID: dbaeumer.vscode-eslint
Descripción: Integrates ESLint JavaScript into VS Code.
Versión: 3.0.10
Editor: Microsoft
Vínculo de VS Marketplace: https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint
```

### ***Categorías de dependencias***

- *En el fichero `package.json`, las dependencias se dividen en dos categorías: `dependencies` y `devDependencies`. Esto se debe a que algunas dependencias solo se utilizan para mejorar la experiencia de desarrollo y no son necesarias para el software en producción.*

```json
{
  "dependencies": {
    "picocolors": "1.0.1"
  },
  "devDependencies": {
    "standard": "17.1.0"
  }
}
```

## ***Configuración de ESLint y VS Code***

### ***Configuración en el `package.json`***

- *Para configurar ESLint en tu proyecto y extender las reglas de estilo de StandardJS, agrega lo siguiente en tu fichero `package.json`:*

```json
{
  "name": "nodejs",
  "version": "1.0.0",
  "description": "Guía Node.js",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "repository": {
    "type": "git",
    "url": "git+ssh://git@github.com/D4nitrix13/Node-JS.git"
  },
  "keywords": [
    "nodejs",
    "node"
  ],
  "author": "Daniel Benjamin Perez Morales - D4nitrix13",
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/D4nitrix13/Node-JS/issues"
  },
  "homepage": "https://github.com/D4nitrix13/Node-JS#readme",
  "dependencies": {
    "picocolors": "1.0.1"
  },
  "devDependencies": {
    "standard": "17.1.0"
  },
  "eslintConfig": {
    "extends": "./node_modules/standard/eslintrc.json"
  }
}
```

### ***Explicación de la configuración en `package.json`***

- *La sección `"eslintConfig"` indica a ESLint que extienda las reglas de estilo definidas en el fichero `eslintrc.json` de StandardJS, que se encuentra en el directorio `node_modules/standard/`.*

### ***Configuración en el fichero `settings.json` de VS Code***

**Para integrar ESLint con VS Code y configurar el comportamiento del editor, puedes agregar las siguientes configuraciones en tu fichero `settings.json` de VS Code:**

```json
{
  "[javascript]": {
    "editor.defaultFormatter": "dbaeumer.vscode-eslint"
  },
  "eslint.format.enable": true,
  "editor.codeActionsOnSave": {
    "source.fixAll": "explicit",
    "source.organizeImports": "explicit"
  },
  "files.autoSave": "afterDelay",
  "editor.formatOnSave": true
}
```

### ***Explicación de las configuraciones en `settings.json`***

- **`[javascript]`:**
  - **`"editor.defaultFormatter"`:** *Define el formateador por defecto para ficheros JavaScript. En este caso, se utiliza `dbaeumer.vscode-eslint`, lo que indica que ESLint se utilizará para formatear el código automáticamente.*

- **`eslint.format.enable`:**
  - *Habilita el formateo del código utilizando ESLint en VS Code.*

- **`editor.codeActionsOnSave`:**
  - **`"source.fixAll"`:** *Configura VS Code para que aplique automáticamente todas las correcciones disponibles al guardar (`explicit` indica que las acciones deben ser explícitamente activadas).*
  - **`"source.organizeImports"`:** *Organiza automáticamente las importaciones al guardar el fichero.*

- **`files.autoSave`:**
  - **`"afterDelay"`:** *Guarda automáticamente los cambios después de un breve retraso.*

- **`editor.formatOnSave`:**
  - *Habilita el formateo automático del código al guardar el fichero en VS Code.*

### ***Funcionalidad de las configuraciones***

- *Estas configuraciones mejoran significativamente el flujo de trabajo de desarrollo al automatizar el formateo del código y la corrección de errores según las reglas de estilo definidas por ESLint y StandardJS. Esto asegura que el código mantenga una consistencia y calidad alta, facilitando así la colaboración y mantenimiento del proyecto.*
