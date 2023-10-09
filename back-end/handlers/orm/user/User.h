//
// User.h
//
// This file has been generated from user.xml. Do not edit.
//


#ifndef DatabaseSystem_User_INCLUDED
#define DatabaseSystem_User_INCLUDED


#include "Poco/ActiveRecord/ActiveRecord.h"


namespace DatabaseSystem {


class User: public Poco::ActiveRecord::ActiveRecord<std::string>
{
public:
	using Ptr = Poco::AutoPtr<User>;

	explicit User(ID id);
	User() = default;
	User(const User& other);
	~User() = default;

	const std::string& password() const;
	User& password(const std::string& value);

	const std::string& salt() const;
	User& salt(const std::string& value);

	static Ptr find(Poco::ActiveRecord::Context::Ptr pContext, const ID& id);

	void insert();
	void update();
	void remove();

	static const std::vector<std::string>& columns();
	static const std::string& table();

private:
	std::string _password;
	std::string _salt;

	friend class Poco::Data::TypeHandler<User>;
};


inline const std::string& User::password() const
{
	return _password;
}


inline User& User::password(const std::string& value)
{
	_password = value;
	return *this;
}


inline const std::string& User::salt() const
{
	return _salt;
}


inline User& User::salt(const std::string& value)
{
	_salt = value;
	return *this;
}


} // namespace DatabaseSystem


namespace Poco {
namespace Data {


template <>
class TypeHandler<DatabaseSystem::User>
{
public:
	static std::size_t size()
	{
		return 2;
	}

	static void bind(std::size_t pos, const DatabaseSystem::User& ar, AbstractBinder::Ptr pBinder, AbstractBinder::Direction dir)
	{
		TypeHandler<std::string>::bind(pos++, ar._password, pBinder, dir);
		TypeHandler<std::string>::bind(pos++, ar._salt, pBinder, dir);
}

	static void extract(std::size_t pos, DatabaseSystem::User& ar, const DatabaseSystem::User& deflt, AbstractExtractor::Ptr pExtr)
	{
		TypeHandler<std::string>::extract(pos++, ar._password, deflt._password, pExtr);
		TypeHandler<std::string>::extract(pos++, ar._salt, deflt._salt, pExtr);
}

	static void prepare(std::size_t pos, const DatabaseSystem::User& ar, AbstractPreparator::Ptr pPrep)
	{
		TypeHandler<std::string>::prepare(pos++, ar._password, pPrep);
		TypeHandler<std::string>::prepare(pos++, ar._salt, pPrep);
	}
};


} } // namespace Poco::Data


#endif // DatabaseSystem_User_INCLUDED
