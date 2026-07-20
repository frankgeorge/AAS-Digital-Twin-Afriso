1. credentials rule
2. nginx and keyrock sever
3. automatically aasx files load to registry server
4. venv instruction readme
5. makefile 
6. ass and asset information about Primovent 


4ea5683d68b3c2703efb22ccf6fe208ec9bedeff6369d84d104bb74440e5d028
Error: creating container storage: the container name "mongo" is already in use by c8f17084e1e22beb16be01c0a672371bdaf7dcc64933bf033447a4cf84f07a38. You have to remove that container to be able to reuse that name: that name is already in use
Error: running container create option: container has joined pod 4ea5683d68b3c2703efb22ccf6fe208ec9bedeff6369d84d104bb74440e5d028 and dependency container c8f17084e1e22beb16be01c0a672371bdaf7dcc64933bf033447a4cf84f07a38 is not a member of the pod: invalid argument
Error: running container create option: container has joined pod 4ea5683d68b3c2703efb22ccf6fe208ec9bedeff6369d84d104bb74440e5d028 and dependency container c8f17084e1e22beb16be01c0a672371bdaf7dcc64933bf033447a4cf84f07a38 is not a member of the pod: invalid argument
Error: running container create option: container has joined pod 4ea5683d68b3c2703efb22ccf6fe208ec9bedeff6369d84d104bb74440e5d028 and dependency container c8f17084e1e22beb16be01c0a672371bdaf7dcc64933bf033447a4cf84f07a38 is not a member of the pod: invalid argument
Error: running container create option: container has joined pod 4ea5683d68b3c2703efb22ccf6fe208ec9bedeff6369d84d104bb74440e5d028 and dependency container c8f17084e1e22beb16be01c0a672371bdaf7dcc64933bf033447a4cf84f07a38 is not a member of the pod: invalid argument
Trying to pull docker.io/eclipsebasyx/aas-gui:latest...
Getting image source signatures
Copying blob sha256:ce42635eeddd348e8266227a36db92cea8a45d5177d03e9a922a7bfb25762b7f
Copying blob sha256:c16defe09b2f86b04c4143bb610095be90732794fce5c56fb7185f02feadd879
Copying blob sha256:967885d218c57d3ce2a4e906131fb25f59e6f56cce51d87dde7d74b0e7465675
Copying blob sha256:e6f31ffc071e5560b82a8685fba8214954e5721e3e49269d00958316edbe89fe
Copying blob sha256:5b429a43b8dfa079c3ac95537bd88d5f1ac70e478c64f100b8ef6aa9c555ebc2
Copying blob sha256:ab1fd90497517c799d4fb351bc1a7ae8b58e231345d4948ae8ac73c75b320b35
Copying blob sha256:01bf363d61e6136ebd7dcaf74b303bd08ee8f849a04e2c0be5a8d03159b404f6
Copying blob sha256:ac3c1a9851c916d88746fc4aea3055e5bd7c4f2e46570a83de81be8c3295b8e4
Copying blob sha256:84d038939923de3f0009dcb86156000b23103896237386b885b827adcb414083
Copying blob sha256:d581532df5ec7bd760dea6891f058ac00916411fd64a943ec5660c6f71a245d9
Copying blob sha256:0afc51df2cfb503f92d5dbc77b011eafa3a33f73ce339ebc78cc87cb230428da
Copying blob sha256:95cebc912086878335c9fc8f0bec08e43e306e592e985eded0874672ddb3da15
Copying blob sha256:d3a07757cc8e5040b078ca6885e6394fa489253ce5a6daa10c35ad81d8f99631
Copying blob sha256:2d5a338abc8f29e37e058f1c3963939c56e97f3b328fc16755628d4321465c27
Copying blob sha256:e20ec0377a6f20794e578387f179f63210f72deed97b736145212f027cabd4da
Copying blob sha256:5ac38b9ad5a16e591639b7ce4f1c4bb56e3dcbde9c93a441702346f29e0d25a9
Copying blob sha256:c62acec5e91049c31db31ecc2f0f313ecc1efc9525d091f6df183323028c5c09
Copying config sha256:752b539a280c209230ce682a02bec7b3514e7bb03ea64467a0ba2db201b384af
Writing manifest to image destination
Error: "machine1-aas" is not a valid container, cannot be used as a dependency: no container with name or ID "machine1-aas" found: no such container
mongo
^CTraceback (most recent call last):
  File "/Users/JisooKim/jisoo/.venv/bin/podman-compose", line 6, in <module>
    sys.exit(main())
  File "/Users/JisooKim/jisoo/.venv/lib/python3.9/site-packages/podman_compose.py", line 4970, in main
    asyncio.run(async_main())
  File "/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/asyncio/base_events.py", line 629, in run_until_complete
    self.run_forever()
  File "/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/asyncio/base_events.py", line 596, in run_forever
    self._run_once()
  File "/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/asyncio/base_events.py", line 1854, in _run_once
    event_list = self._selector.select(timeout)
  File "/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/selectors.py", line 562, in select
    kev_list = self._selector.control(None, max_ev, timeout)
KeyboardInterrupt
Exception ignored in: <function BaseSubprocessTransport.__del__ at 0x107635670>
Traceback (most recent call last):
  File "/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/asyncio/base_subprocess.py", line 126, in __del__
  File "/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/asyncio/base_subprocess.py", line 104, in close
  File "/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/asyncio/unix_events.py", line 536, in close
  File "/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/asyncio/unix_events.py", line 560, in _close
  File "/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/asyncio/base_events.py", line 746, in call_soon
  File "/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/asyncio/base_events.py", line 510, in _check_closed