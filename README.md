# DiuResult
<h1> Installation Process: </h1>
<ol>
<li><p> Download The released Exe File. that's it</P></li>
<li><p>Double click on DiuResult.exe to run</P></li>
</ol>

# For CommandLine Argument Use Go to Main Branch
Main Branch : https://github.com/grim-firefly/DiuResult/tree/main
# How it's Work
<ol>
  <li>Open cmd inside project directory again and write <code> double click on DiuResult.exe </code>. This will explain common flags</li>
<li>
  Here is The Flags:
  <ul>
    <li>-h: command  <code> -h</code> . this will open the documentation to use </li>
    <li>-id: use this flag to initilize some id . command <code>-id 191-35-407 191-35-441</code>. You can input multiple id as you like..
    <li>-range: use this flag to give a range of id as input : command : <code> -range 191-35-404 191-35-407</code> .this will input all id <code>[191-35-404,191-35-405,191-35-406,191-35-407]</code>. You can specify multiple range like <code>-range 191-35-404 191-35-407 191-35-410 191-35-413</code>.this will input all id <code>[191-35-404,191-35-405,191-35-406,191-35-407] </code> and<code> [191-35-410,191-35-4111,191-35-412,191-35-413]</code>   </li>
    <li>-sem: use this flag if you want some specific semester result. ususage <code>-id 191-35-407 -sem 191 192 193</code>. you can give multiple semester as input. Remember Here <code>191-> spring 2019 , 192->summer 2019 , 193->fall 2019</code>. Semester contains 3 digit, first 2 digit is year's last 2 digit and last digit means <code>spring=1, summer=2, fall=3</code>.<b> If you don't specify any semester, this script use all the semester as default perameter</b></li>
    <li>-f: use this flag when you want to specify id from a file . usuage : <code>-f allid.txt</code> .this will ake all id from <b>allid.txt</b> file. 
    You can write id in 2 way in file :
      <ol type="i">
        <li> <code>191-35-407</code> </li>
        <li><code>-range 191-35-401 191-35-407</code></li>
      </ol>
      <p> but you can't write like </p>
      <ol type="i">
        <li> <code>191-35-405 191-35-406 191-35-407</code> </li>
        <li><code>-range 191-35-401 191-35-407 191-35-410 191-35-417</code> </li>
      </ol>
      </li>
    <li>-together: this flag has no perameter. use this flag i you want to combine output in a file command: <code>-range 191-35-401 191-35-407 -sem 191 -together </code>. This command will retrive all the result of this range and add in a single file <code>output.html</code>. If you don't use this flag. This script will create result of individual id's in a individual file. like <code>191-35-407.html 191-35-441.html</code> </li>
    <li><b> <i> Default output directory is Output inside the program directory</i> </b> </li>
    
  </ul>

  </li>
</ol>

# Some Example
<ul>
<li><p>retriving some ids result of all semester <code>-id 191-35-407 191-35-441 191-35-405 191-35-427 </code> . this will retrive all semester result of all those ids and create file <code> 191-35-407.html 191-35-441.html 191-35-405.html 191-35-427.html</code> </p></li>

<li><p>retriving some ids result of spring 2019 semester <code>-id 191-35-407 191-35-441 191-35-405 191-35-427 -sem 191 </code> . this will retrive spring 2019 semester result of all those ids and create file <code> 191-35-407.html 191-35-441.html 191-35-405.html 191-35-427.html</code> </p></li>

<li><p>retriving ranges result of spring 2019 semester <code>-range 191-35-405 191-35-407 -sem 191 </code> . this will retrive spring 2019 semester result of all those ids and create file <code> 191-35-405.html 191-35-406.html 191-35-407.html</code> </p></li>

<li><p>retriving ranges result of spring 2019 semester and put in a single file <code>-range 191-35-401 191-35-441 -sem 191 -together </code> . this will retrive spring 2019 semester result of all id 401 to 441 including 401 and 441 and create a ouput file <code> output.html</code> </p></li>
  
  <li><p>retriving all id from a file and retrive result of spring 2019,summer 2019 fall 2019 and spring 2020  semester and put in a single file <code>-f allids.txt -sem 191 192 193 201 -together </code> . this will retrive spring 2019 semester result of all id 401 to 441 including 401 and 441 and create a ouput file <code> output.html</code> </p></li>
  
</ul>

# Example of a File text
<p><b>allids.txt</b></p> 
  <p><code>191-35-407</code></p> 
  <p><code>191-35-441</code></p> 
 <p><code>-range 191-35-401 191-35-406</code></p> 
 <p><code>-range 191-35-415 191-35-427</code></p> 
 <p><code>191-35-443</code></p> 

