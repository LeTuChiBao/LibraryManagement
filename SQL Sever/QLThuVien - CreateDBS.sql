CREATE DATABASE QLThuVien
GO

USE QLThuVien
GO
CREATE TABLE TheLoai
(
	Id_TheLoai		CHAR(5) not null PRIMARY KEY,
	TenTheLoai		NVARCHAR(100),
)
GO
CREATE TABLE Sach
(
	Id_Sach			CHAR(10) not null PRIMARY KEY,
	TenSach			NVARCHAR(MAX),
	TenTacGia		NVARCHAR(200),
	NhaXB			NVARCHAR(200),
	NamXB			INT,
	Id_TheLoai		CHAR(5) not null FOREIGN KEY REFERENCES TheLoai(Id_TheLoai),
	TenKe			VARCHAR(5),
	GiaSach			VARCHAR(100),
)
GO
CREATE TABLE NguoiDung
(
	Id_NguoiDung	CHAR(10) not null PRIMARY KEY,
	HoTen			NVARCHAR(MAX),
	GioiTinh		NVARCHAR(15),
	NgaySinh		DATETIME,
	SoDT			VARCHAR(15),
	DiaChi			NVARCHAR(200),
	NoiCongTac		NVARCHAR(200),
	Email			NVARCHAR(200),
	VaiTro			NVARCHAR(30),
	NgayThamGia		DATETIME
)
GO
CREATE TABLE DangNhap
(
	TenDangNhap		VARCHAR(20) not null PRIMARY KEY,
	MatKhau			VARCHAR(20) not null,
	Id_NguoiDung	CHAR(10) not null FOREIGN KEY REFERENCES NguoiDung(Id_NguoiDung)
)
GO
CREATE TABLE PhieuMuon
(
	Id_PhieuMuon	CHAR(10) not null PRIMARY KEY,
	Id_NguoiDung	CHAR(10) not null FOREIGN KEY REFERENCES NguoiDung(Id_NguoiDung),
	TongPhiMuon		NVARCHAR(100) DEFAULT (N'Miễn Phí')
)
GO
CREATE TABLE ChiTietPhieuMuon
(
	Id_PhieuMuon	CHAR(10) not null FOREIGN KEY REFERENCES PhieuMuon(Id_PhieuMuon),
	Id_Sach			CHAR(10) not null FOREIGN KEY REFERENCES Sach(Id_Sach),
	NgayMuon		DATETIME,
	NgayTra			DATETIME,
	SoNgayMuon		INT,
	PhiMuon			NVARCHAR(100) DEFAULT (N'Miễn Phí'),
	GhiChu			NVARCHAR(100) DEFAULT (N'Không'),
	Trangthai		NVARCHAR(100) DEFAULT (N'Đã mượn')
	CONSTRAINT PK_CHITIETPHIEUMUON PRIMARY KEY (Id_PhieuMuon,Id_Sach)
)
