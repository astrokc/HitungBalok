uses crt;
var p,l,t : Integer;
nama : string;
begin
clrscr;
writeln ('=====================================');
writeln ('=       PROGRAM VOLUME BALOK        =');
writeln ('=====================================');
readln;
writeln;
write   ('MASUKAN NAMA ANDA       = '); readln(nama);
writeln ('  ','  HAI ',nama,'.....!!  ','');
writeln ('  ',' WELCOME TO MY PROGRAM ','');
writeln;
writeln ('  ','      TEKAN "ENTER"   ','');
writeln (' ','  UNTUK MEMULAI PROGRAM','');
readln;
writeln;
writeln ('-----------------------------------');
write   ('MASUKAN NILAI PANJANG = '); readln(p);
write   ('MASUKAN NILAI LEBAR   = '); readln(l);
write   ('MASUKAN NILAI TINGGI  = '); readln(t);
writeln;
writeln ('  ','      TEKAN "ENTER"    ','');
writeln (' ','  UNTUK MELIHAT HASILNYA','');
readln;
writeln;
writeln ('vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv');
writeln ('VOLUME BALOK ADALAH = ',p*l*t,' cm3');
writeln ('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^');
writeln;
writeln ('TERIMA KASIH ',nama,'');
writeln ('SAMPAI JUMPA .....!');
readln;
end.
