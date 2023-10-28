//
// EmailVerification.h
//
// This file has been generated from pet_adoption.xml. Do not edit.
//


#ifndef DatabaseSystem_EmailVerification_INCLUDED
#define DatabaseSystem_EmailVerification_INCLUDED


#include "Poco/ActiveRecord/ActiveRecord.h"


namespace DatabaseSystem {


class EmailVerification: public Poco::ActiveRecord::ActiveRecord<std::string>
{
public:
	using Ptr = Poco::AutoPtr<EmailVerification>;

	explicit EmailVerification(ID id);
	EmailVerification() = default;
	EmailVerification(const EmailVerification& other);
	~EmailVerification() = default;

	const std::string& emailProof() const;
	EmailVerification& emailProof(const std::string& value);

	const Poco::Timestamp& expirationAt() const;
	EmailVerification& expirationAt(const Poco::Timestamp& value);

	bool used() const;
	EmailVerification& used(bool value);

	static Ptr find(Poco::ActiveRecord::Context::Ptr pContext, const ID& id);

	void insert();
	void update();
	void remove();

	static const std::vector<std::string>& columns();
	static const std::string& table();

private:
	std::string _emailProof;
	Poco::Timestamp _expirationAt;
	bool _used = false;

	friend class Poco::Data::TypeHandler<EmailVerification>;
};


inline const std::string& EmailVerification::emailProof() const
{
	return _emailProof;
}


inline EmailVerification& EmailVerification::emailProof(const std::string& value)
{
	_emailProof = value;
	return *this;
}


inline const Poco::Timestamp& EmailVerification::expirationAt() const
{
	return _expirationAt;
}


inline EmailVerification& EmailVerification::expirationAt(const Poco::Timestamp& value)
{
	_expirationAt = value;
	return *this;
}


inline bool EmailVerification::used() const
{
	return _used;
}


inline EmailVerification& EmailVerification::used(bool value)
{
	_used = value;
	return *this;
}


} // namespace DatabaseSystem


namespace Poco {
namespace Data {


template <>
class TypeHandler<DatabaseSystem::EmailVerification>
{
public:
	static std::size_t size()
	{
		return 3;
	}

	static void bind(std::size_t pos, const DatabaseSystem::EmailVerification& ar, AbstractBinder::Ptr pBinder, AbstractBinder::Direction dir)
	{
		TypeHandler<std::string>::bind(pos++, ar._emailProof, pBinder, dir);
		TypeHandler<Poco::Timestamp>::bind(pos++, ar._expirationAt, pBinder, dir);
		TypeHandler<bool>::bind(pos++, ar._used, pBinder, dir);
}

	static void extract(std::size_t pos, DatabaseSystem::EmailVerification& ar, const DatabaseSystem::EmailVerification& deflt, AbstractExtractor::Ptr pExtr)
	{
		TypeHandler<std::string>::extract(pos++, ar._emailProof, deflt._emailProof, pExtr);
		TypeHandler<Poco::Timestamp>::extract(pos++, ar._expirationAt, deflt._expirationAt, pExtr);
		TypeHandler<bool>::extract(pos++, ar._used, deflt._used, pExtr);
}

	static void prepare(std::size_t pos, const DatabaseSystem::EmailVerification& ar, AbstractPreparator::Ptr pPrep)
	{
		TypeHandler<std::string>::prepare(pos++, ar._emailProof, pPrep);
		TypeHandler<Poco::Timestamp>::prepare(pos++, ar._expirationAt, pPrep);
		TypeHandler<bool>::prepare(pos++, ar._used, pPrep);
	}
};


} } // namespace Poco::Data


#endif // DatabaseSystem_EmailVerification_INCLUDED
